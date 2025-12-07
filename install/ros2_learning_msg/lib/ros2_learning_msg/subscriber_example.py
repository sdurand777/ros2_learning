#!/usr/bin/env python3
"""
Example subscriber node using custom messages.
Subscribes to RobotStatus and SensorData topics.
"""

import rclpy
from rclpy.node import Node
from ros2_learning_msg.msg import RobotStatus, SensorData


class StatusSubscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber')

        # Subscribers
        self.status_sub = self.create_subscription(
            RobotStatus,
            'robot_status',
            self.status_callback,
            10
        )

        self.sensor_sub = self.create_subscription(
            SensorData,
            'sensor_data',
            self.sensor_callback,
            10
        )

        # Store latest data
        self.latest_status = None
        self.latest_sensor = None

        self.get_logger().info('Status Subscriber initialized')

    def status_callback(self, msg: RobotStatus):
        self.latest_status = msg

        mode_names = {
            RobotStatus.MODE_MANUAL: 'MANUAL',
            RobotStatus.MODE_STABILIZE: 'STABILIZE',
            RobotStatus.MODE_DEPTH_HOLD: 'DEPTH_HOLD',
            RobotStatus.MODE_AUTO: 'AUTO'
        }

        self.get_logger().info(
            f'Robot: {msg.robot_name} | '
            f'Pos: ({msg.position.x:.2f}, {msg.position.y:.2f}, {msg.position.z:.2f}) | '
            f'Mode: {mode_names.get(msg.mode, "UNKNOWN")} | '
            f'Armed: {msg.is_armed} | '
            f'Battery: {msg.battery_level:.1f}%'
        )

    def sensor_callback(self, msg: SensorData):
        self.latest_sensor = msg

        self.get_logger().debug(
            f'Sensors | '
            f'Depth: {msg.depth:.2f}m | '
            f'Pressure: {msg.pressure:.0f}Pa | '
            f'Temp: {msg.temperature:.1f}°C | '
            f'Valid: {msg.is_valid}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
