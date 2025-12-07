#!/usr/bin/env python3
"""
Example publisher node using custom messages.
Publishes RobotStatus messages at 10 Hz.
"""

import rclpy
from rclpy.node import Node
from ros2_learning_msg.msg import RobotStatus, SensorData
from geometry_msgs.msg import Point, Quaternion, Twist, Vector3
from std_msgs.msg import Header
import math
import time


class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')

        # Publishers
        self.status_pub = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.sensor_pub = self.create_publisher(SensorData, 'sensor_data', 10)

        # Timer for publishing at 10 Hz
        self.timer = self.create_timer(0.1, self.timer_callback)

        # State variables
        self.counter = 0
        self.start_time = time.time()

        self.get_logger().info('Status Publisher initialized')

    def timer_callback(self):
        # Calculate elapsed time for simulated motion
        elapsed = time.time() - self.start_time

        # Create and publish RobotStatus
        status_msg = RobotStatus()
        status_msg.header = Header()
        status_msg.header.stamp = self.get_clock().now().to_msg()
        status_msg.header.frame_id = 'base_link'

        status_msg.robot_name = 'bluerov2'
        status_msg.robot_id = 1

        # Simulated circular motion
        status_msg.position = Point(
            x=5.0 * math.cos(elapsed * 0.5),
            y=5.0 * math.sin(elapsed * 0.5),
            z=-2.0  # 2 meters depth
        )

        status_msg.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        status_msg.velocity = Twist()
        status_msg.velocity.linear = Vector3(x=0.5, y=0.0, z=0.0)
        status_msg.velocity.angular = Vector3(x=0.0, y=0.0, z=0.1)

        status_msg.battery_level = max(0.0, 100.0 - elapsed * 0.1)
        status_msg.is_armed = True
        status_msg.is_connected = True
        status_msg.mode = RobotStatus.MODE_DEPTH_HOLD

        self.status_pub.publish(status_msg)

        # Create and publish SensorData
        sensor_msg = SensorData()
        sensor_msg.header = status_msg.header

        sensor_msg.acceleration = Vector3(x=0.01, y=-0.02, z=-9.81)
        sensor_msg.gyroscope = Vector3(x=0.001, y=0.002, z=0.1)
        sensor_msg.magnetometer = Vector3(x=0.25, y=0.05, z=0.4)

        sensor_msg.pressure = 101325.0 + (abs(status_msg.position.z) * 10000)
        sensor_msg.depth = abs(status_msg.position.z)
        sensor_msg.temperature = 18.5

        sensor_msg.latitude = 43.6047
        sensor_msg.longitude = 1.4442
        sensor_msg.altitude = 0.0

        sensor_msg.is_valid = True
        sensor_msg.confidence = 0.95

        self.sensor_pub.publish(sensor_msg)

        self.counter += 1
        if self.counter % 50 == 0:
            self.get_logger().info(
                f'Published {self.counter} messages, '
                f'depth: {sensor_msg.depth:.2f}m, '
                f'battery: {status_msg.battery_level:.1f}%'
            )


def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
