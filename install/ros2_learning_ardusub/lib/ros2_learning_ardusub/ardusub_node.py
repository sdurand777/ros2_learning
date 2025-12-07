#!/usr/bin/env python3
"""
ArduSub Main Node.
Connects to ArduSub autopilot via MAVLink and provides ROS2 interface.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
from sensor_msgs.msg import Imu, BatteryState
from std_msgs.msg import Float64, Bool, UInt8
from std_srvs.srv import SetBool, Trigger

try:
    from pymavlink import mavutil
    PYMAVLINK_AVAILABLE = True
except ImportError:
    PYMAVLINK_AVAILABLE = False
    print("Warning: pymavlink not installed. Running in simulation mode.")


class ArduSubNode(Node):
    """Main ArduSub ROS2 interface node."""

    # ArduSub flight modes
    MODES = {
        0: 'STABILIZE',
        1: 'ACRO',
        2: 'ALT_HOLD',
        3: 'AUTO',
        4: 'GUIDED',
        5: 'CIRCLE',
        7: 'SURFACE',
        9: 'POSHOLD',
        16: 'MANUAL',
        19: 'DEPTH_HOLD'
    }

    def __init__(self):
        super().__init__('ardusub_node')

        # Declare parameters
        self.declare_parameter('connection_string', 'udpin:0.0.0.0:14550')
        self.declare_parameter('baudrate', 115200)
        self.declare_parameter('source_system', 255)
        self.declare_parameter('heartbeat_rate', 1.0)
        self.declare_parameter('telemetry_rate', 10.0)

        self.connection_string = self.get_parameter('connection_string').value
        self.baudrate = self.get_parameter('baudrate').value
        self.source_system = self.get_parameter('source_system').value

        # State
        self.mav = None
        self.connected = False
        self.armed = False
        self.mode = 'UNKNOWN'
        self.battery_voltage = 0.0
        self.battery_current = 0.0

        # Publishers
        self.pose_pub = self.create_publisher(PoseStamped, 'pose', 10)
        self.imu_pub = self.create_publisher(Imu, 'imu/data', 10)
        self.battery_pub = self.create_publisher(BatteryState, 'battery', 10)
        self.depth_pub = self.create_publisher(Float64, 'depth', 10)
        self.armed_pub = self.create_publisher(Bool, 'armed', 10)
        self.mode_pub = self.create_publisher(UInt8, 'mode', 10)

        # Subscribers
        self.cmd_vel_sub = self.create_subscription(
            Twist, 'cmd_vel', self.cmd_vel_callback, 10
        )

        # Services
        self.arm_srv = self.create_service(SetBool, 'arm', self.arm_callback)
        self.dive_srv = self.create_service(Trigger, 'dive', self.dive_callback)
        self.surface_srv = self.create_service(Trigger, 'surface', self.surface_callback)

        # Timers
        heartbeat_period = 1.0 / self.get_parameter('heartbeat_rate').value
        self.heartbeat_timer = self.create_timer(heartbeat_period, self.send_heartbeat)

        telemetry_period = 1.0 / self.get_parameter('telemetry_rate').value
        self.telemetry_timer = self.create_timer(telemetry_period, self.read_telemetry)

        # Connect to vehicle
        self.connect()

        self.get_logger().info(f'ArduSub Node initialized')
        self.get_logger().info(f'Connection: {self.connection_string}')

    def connect(self):
        """Connect to ArduSub via MAVLink."""
        if not PYMAVLINK_AVAILABLE:
            self.get_logger().warn('pymavlink not available - running in simulation mode')
            return

        try:
            self.get_logger().info(f'Connecting to {self.connection_string}...')
            self.mav = mavutil.mavlink_connection(
                self.connection_string,
                baud=self.baudrate,
                source_system=self.source_system
            )

            # Wait for heartbeat
            self.get_logger().info('Waiting for heartbeat...')
            self.mav.wait_heartbeat(timeout=10)
            self.connected = True
            self.get_logger().info(
                f'Connected to system {self.mav.target_system}, '
                f'component {self.mav.target_component}'
            )

            # Request data streams
            self.request_data_streams()

        except Exception as e:
            self.get_logger().error(f'Connection failed: {e}')
            self.connected = False

    def request_data_streams(self):
        """Request MAVLink data streams from autopilot."""
        if not self.mav:
            return

        # Request all streams at 10 Hz
        self.mav.mav.request_data_stream_send(
            self.mav.target_system,
            self.mav.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_ALL,
            10,  # Rate Hz
            1    # Start
        )

    def send_heartbeat(self):
        """Send heartbeat to autopilot."""
        if not self.mav or not self.connected:
            return

        try:
            self.mav.mav.heartbeat_send(
                mavutil.mavlink.MAV_TYPE_GCS,
                mavutil.mavlink.MAV_AUTOPILOT_INVALID,
                0, 0, 0
            )
        except Exception as e:
            self.get_logger().debug(f'Heartbeat send error: {e}')

    def read_telemetry(self):
        """Read and publish telemetry from autopilot."""
        if not self.mav or not self.connected:
            self._publish_simulated_telemetry()
            return

        try:
            # Non-blocking read
            msg = self.mav.recv_match(blocking=False)
            while msg:
                self._process_mavlink_message(msg)
                msg = self.mav.recv_match(blocking=False)
        except Exception as e:
            self.get_logger().debug(f'Telemetry read error: {e}')

    def _process_mavlink_message(self, msg):
        """Process incoming MAVLink message."""
        msg_type = msg.get_type()

        if msg_type == 'HEARTBEAT':
            self.armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
            self.mode = self.MODES.get(msg.custom_mode, 'UNKNOWN')

            armed_msg = Bool()
            armed_msg.data = self.armed
            self.armed_pub.publish(armed_msg)

            mode_msg = UInt8()
            mode_msg.data = msg.custom_mode
            self.mode_pub.publish(mode_msg)

        elif msg_type == 'SCALED_PRESSURE':
            depth_msg = Float64()
            # Convert pressure to depth (assuming fresh water)
            depth_msg.data = (msg.press_abs - 101325) / 9810.0
            self.depth_pub.publish(depth_msg)

        elif msg_type == 'RAW_IMU':
            imu_msg = Imu()
            imu_msg.header.stamp = self.get_clock().now().to_msg()
            imu_msg.header.frame_id = 'imu_link'

            # Scale raw values (ArduPilot uses millig and millirad/s)
            imu_msg.linear_acceleration.x = msg.xacc / 1000.0 * 9.81
            imu_msg.linear_acceleration.y = msg.yacc / 1000.0 * 9.81
            imu_msg.linear_acceleration.z = msg.zacc / 1000.0 * 9.81

            imu_msg.angular_velocity.x = msg.xgyro / 1000.0
            imu_msg.angular_velocity.y = msg.ygyro / 1000.0
            imu_msg.angular_velocity.z = msg.zgyro / 1000.0

            self.imu_pub.publish(imu_msg)

        elif msg_type == 'SYS_STATUS':
            battery_msg = BatteryState()
            battery_msg.voltage = msg.voltage_battery / 1000.0
            battery_msg.current = msg.current_battery / 100.0
            battery_msg.percentage = msg.battery_remaining / 100.0
            self.battery_pub.publish(battery_msg)

    def _publish_simulated_telemetry(self):
        """Publish simulated telemetry when not connected."""
        # Simulated depth
        depth_msg = Float64()
        depth_msg.data = 2.0
        self.depth_pub.publish(depth_msg)

        # Simulated armed state
        armed_msg = Bool()
        armed_msg.data = self.armed
        self.armed_pub.publish(armed_msg)

    def cmd_vel_callback(self, msg: Twist):
        """Handle velocity commands."""
        if not self.mav or not self.connected:
            self.get_logger().debug('Not connected - cmd_vel ignored')
            return

        if not self.armed:
            self.get_logger().warn('Not armed - cmd_vel ignored')
            return

        # Send RC override or manual control
        self._send_manual_control(msg)

    def _send_manual_control(self, twist: Twist):
        """Send manual control command to autopilot."""
        # Scale twist to -1000 to 1000 range
        x = int(twist.linear.x * 1000)
        y = int(twist.linear.y * 1000)
        z = int((twist.linear.z + 1) * 500)  # 0-1000, 500 = neutral
        r = int(twist.angular.z * 1000)

        # Clamp values
        x = max(-1000, min(1000, x))
        y = max(-1000, min(1000, y))
        z = max(0, min(1000, z))
        r = max(-1000, min(1000, r))

        self.mav.mav.manual_control_send(
            self.mav.target_system,
            x, y, z, r,
            0  # buttons
        )

    def arm_callback(self, request, response):
        """Arm/disarm service callback."""
        if request.data:
            success = self._arm()
            response.success = success
            response.message = 'Armed' if success else 'Arm failed'
        else:
            success = self._disarm()
            response.success = success
            response.message = 'Disarmed' if success else 'Disarm failed'
        return response

    def _arm(self) -> bool:
        """Arm the vehicle."""
        if not self.mav or not self.connected:
            self.get_logger().warn('Cannot arm - not connected')
            self.armed = True  # Simulate in disconnected mode
            return True

        self.mav.arducopter_arm()
        self.mav.motors_armed_wait()
        self.armed = True
        self.get_logger().info('Vehicle armed')
        return True

    def _disarm(self) -> bool:
        """Disarm the vehicle."""
        if not self.mav or not self.connected:
            self.armed = False
            return True

        self.mav.arducopter_disarm()
        self.mav.motors_disarmed_wait()
        self.armed = False
        self.get_logger().info('Vehicle disarmed')
        return True

    def dive_callback(self, request, response):
        """Dive to depth service callback."""
        self.get_logger().info('Dive command received')
        response.success = True
        response.message = 'Diving...'
        return response

    def surface_callback(self, request, response):
        """Surface service callback."""
        self.get_logger().info('Surface command received')
        response.success = True
        response.message = 'Surfacing...'
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ArduSubNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
