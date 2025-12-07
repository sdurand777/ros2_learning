#!/usr/bin/env python3
"""
Telemetry Publisher Node.
Publishes simulated ArduSub telemetry for testing without real hardware.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, BatteryState
from geometry_msgs.msg import PoseStamped, TwistStamped
from std_msgs.msg import Float64, Bool, UInt8
from nav_msgs.msg import Odometry
import math
import time
import random


class TelemetryPublisher(Node):
    """Publishes simulated ArduSub telemetry."""

    def __init__(self):
        super().__init__('telemetry_publisher')

        # Parameters
        self.declare_parameter('rate', 50.0)
        self.declare_parameter('noise_level', 0.01)

        self.rate = self.get_parameter('rate').value
        self.noise = self.get_parameter('noise_level').value

        # Simulated state
        self.position = [0.0, 0.0, -2.0]  # x, y, z (depth)
        self.velocity = [0.0, 0.0, 0.0]
        self.orientation = [0.0, 0.0, 0.0, 1.0]  # quaternion
        self.euler = [0.0, 0.0, 0.0]  # roll, pitch, yaw
        self.armed = False
        self.mode = 0
        self.battery_voltage = 16.8
        self.battery_current = 5.0
        self.start_time = time.time()

        # Publishers
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)
        self.pose_pub = self.create_publisher(PoseStamped, 'pose', 10)
        self.imu_pub = self.create_publisher(Imu, 'imu/data', 10)
        self.battery_pub = self.create_publisher(BatteryState, 'battery', 10)
        self.depth_pub = self.create_publisher(Float64, 'depth', 10)
        self.heading_pub = self.create_publisher(Float64, 'heading', 10)
        self.armed_pub = self.create_publisher(Bool, 'armed', 10)
        self.mode_pub = self.create_publisher(UInt8, 'mode', 10)

        # Subscribers (for simulating response to commands)
        self.cmd_vel_sub = self.create_subscription(
            TwistStamped, 'cmd_vel', self.cmd_vel_callback, 10
        )

        # Timer
        self.timer = self.create_timer(1.0 / self.rate, self.publish_telemetry)
        self.battery_timer = self.create_timer(1.0, self.update_battery)

        self.get_logger().info('Telemetry Publisher initialized (simulation mode)')

    def cmd_vel_callback(self, msg):
        """Update simulated velocity from commands."""
        self.velocity[0] = msg.twist.linear.x
        self.velocity[1] = msg.twist.linear.y
        self.velocity[2] = msg.twist.linear.z

    def euler_to_quaternion(self, roll, pitch, yaw):
        """Convert Euler angles to quaternion."""
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        return [
            sr * cp * cy - cr * sp * sy,  # x
            cr * sp * cy + sr * cp * sy,  # y
            cr * cp * sy - sr * sp * cy,  # z
            cr * cp * cy + sr * sp * sy   # w
        ]

    def update_simulation(self, dt):
        """Update simulated state."""
        # Simulate gentle motion
        elapsed = time.time() - self.start_time

        # Circular path
        self.position[0] = 3.0 * math.cos(elapsed * 0.1)
        self.position[1] = 3.0 * math.sin(elapsed * 0.1)
        self.position[2] = -2.0 - 0.5 * math.sin(elapsed * 0.2)  # Slight depth variation

        # Orientation follows velocity
        self.euler[2] = math.atan2(self.velocity[1], self.velocity[0] + 0.001)
        self.euler[0] = 0.02 * math.sin(elapsed * 0.5)  # Small roll
        self.euler[1] = 0.01 * math.sin(elapsed * 0.3)  # Small pitch

        self.orientation = self.euler_to_quaternion(*self.euler)

    def add_noise(self, value, scale=1.0):
        """Add Gaussian noise to a value."""
        return value + random.gauss(0, self.noise * scale)

    def publish_telemetry(self):
        """Publish all telemetry."""
        now = self.get_clock().now()
        dt = 1.0 / self.rate

        self.update_simulation(dt)

        # Odometry
        odom = Odometry()
        odom.header.stamp = now.to_msg()
        odom.header.frame_id = 'world'
        odom.child_frame_id = 'base_link'
        odom.pose.pose.position.x = self.add_noise(self.position[0])
        odom.pose.pose.position.y = self.add_noise(self.position[1])
        odom.pose.pose.position.z = self.add_noise(self.position[2])
        odom.pose.pose.orientation.x = self.orientation[0]
        odom.pose.pose.orientation.y = self.orientation[1]
        odom.pose.pose.orientation.z = self.orientation[2]
        odom.pose.pose.orientation.w = self.orientation[3]
        odom.twist.twist.linear.x = self.add_noise(self.velocity[0])
        odom.twist.twist.linear.y = self.add_noise(self.velocity[1])
        odom.twist.twist.linear.z = self.add_noise(self.velocity[2])
        self.odom_pub.publish(odom)

        # Pose
        pose = PoseStamped()
        pose.header = odom.header
        pose.pose = odom.pose.pose
        self.pose_pub.publish(pose)

        # IMU
        imu = Imu()
        imu.header.stamp = now.to_msg()
        imu.header.frame_id = 'imu_link'
        imu.orientation.x = self.orientation[0]
        imu.orientation.y = self.orientation[1]
        imu.orientation.z = self.orientation[2]
        imu.orientation.w = self.orientation[3]
        imu.angular_velocity.x = self.add_noise(0.0, 0.1)
        imu.angular_velocity.y = self.add_noise(0.0, 0.1)
        imu.angular_velocity.z = self.add_noise(0.1)  # Slight yaw rate
        imu.linear_acceleration.x = self.add_noise(0.0, 0.5)
        imu.linear_acceleration.y = self.add_noise(0.0, 0.5)
        imu.linear_acceleration.z = self.add_noise(-9.81, 0.5)
        self.imu_pub.publish(imu)

        # Depth
        depth = Float64()
        depth.data = abs(self.add_noise(self.position[2], 0.1))
        self.depth_pub.publish(depth)

        # Heading
        heading = Float64()
        heading.data = self.euler[2]
        self.heading_pub.publish(heading)

        # Armed state
        armed = Bool()
        armed.data = self.armed
        self.armed_pub.publish(armed)

        # Mode
        mode = UInt8()
        mode.data = self.mode
        self.mode_pub.publish(mode)

    def update_battery(self):
        """Update simulated battery state."""
        # Slow discharge
        self.battery_voltage = max(14.0, self.battery_voltage - 0.001)

        battery = BatteryState()
        battery.voltage = self.add_noise(self.battery_voltage, 0.1)
        battery.current = self.add_noise(self.battery_current, 0.5)
        battery.percentage = (self.battery_voltage - 14.0) / (16.8 - 14.0)
        battery.present = True
        self.battery_pub.publish(battery)


def main(args=None):
    rclpy.init(args=args)
    node = TelemetryPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
