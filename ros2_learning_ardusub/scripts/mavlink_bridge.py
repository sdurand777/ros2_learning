#!/usr/bin/env python3
"""
MAVLink Bridge Node.
Provides a bridge between MAVLink and ROS2 topics.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, UInt16MultiArray
import threading
import time

try:
    from pymavlink import mavutil
    PYMAVLINK_AVAILABLE = True
except ImportError:
    PYMAVLINK_AVAILABLE = False


class MAVLinkBridge(Node):
    """Bridge between MAVLink and ROS2."""

    def __init__(self):
        super().__init__('mavlink_bridge')

        # Parameters
        self.declare_parameter('connection', 'udpin:0.0.0.0:14550')
        self.declare_parameter('baudrate', 115200)
        self.declare_parameter('fcu_url', 'udp://:14540@:14557')

        self.connection = self.get_parameter('connection').value

        # MAVLink connection
        self.mav = None
        self.running = True

        # Publishers
        self.raw_mavlink_pub = self.create_publisher(String, 'mavlink/raw', 100)
        self.rc_channels_pub = self.create_publisher(UInt16MultiArray, 'mavlink/rc_channels', 10)

        # Subscribers
        self.rc_override_sub = self.create_subscription(
            UInt16MultiArray, 'mavlink/rc_override', self.rc_override_callback, 10
        )

        # Connect
        if PYMAVLINK_AVAILABLE:
            self.connect_mavlink()

            # Start receive thread
            self.receive_thread = threading.Thread(target=self.receive_loop, daemon=True)
            self.receive_thread.start()
        else:
            self.get_logger().warn('pymavlink not available')

        self.get_logger().info('MAVLink Bridge initialized')

    def connect_mavlink(self):
        """Establish MAVLink connection."""
        try:
            self.get_logger().info(f'Connecting to {self.connection}...')
            self.mav = mavutil.mavlink_connection(self.connection)
            self.mav.wait_heartbeat(timeout=30)
            self.get_logger().info('MAVLink connected')
        except Exception as e:
            self.get_logger().error(f'Connection failed: {e}')

    def receive_loop(self):
        """Background thread for receiving MAVLink messages."""
        while self.running and self.mav:
            try:
                msg = self.mav.recv_match(blocking=True, timeout=1.0)
                if msg:
                    self.process_message(msg)
            except Exception as e:
                self.get_logger().debug(f'Receive error: {e}')
                time.sleep(0.1)

    def process_message(self, msg):
        """Process received MAVLink message."""
        msg_type = msg.get_type()

        # Publish raw message as JSON-like string
        raw_msg = String()
        raw_msg.data = f'{{"type": "{msg_type}", "data": {msg.to_dict()}}}'
        self.raw_mavlink_pub.publish(raw_msg)

        # Process specific message types
        if msg_type == 'RC_CHANNELS':
            rc_msg = UInt16MultiArray()
            rc_msg.data = [
                msg.chan1_raw, msg.chan2_raw, msg.chan3_raw, msg.chan4_raw,
                msg.chan5_raw, msg.chan6_raw, msg.chan7_raw, msg.chan8_raw
            ]
            self.rc_channels_pub.publish(rc_msg)

    def rc_override_callback(self, msg: UInt16MultiArray):
        """Send RC override commands."""
        if not self.mav:
            return

        channels = list(msg.data) + [0] * (8 - len(msg.data))

        self.mav.mav.rc_channels_override_send(
            self.mav.target_system,
            self.mav.target_component,
            *channels[:8]
        )

    def destroy_node(self):
        """Clean up on shutdown."""
        self.running = False
        if self.mav:
            self.mav.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = MAVLinkBridge()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
