#!/usr/bin/env python3
"""
Example service client using custom services.
Calls GetStatus and SetCommand services.
"""

import rclpy
from rclpy.node import Node
from ros2_learning_msg.srv import GetStatus, SetCommand
from ros2_learning_msg.msg import RobotStatus
import sys


class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')

        # Service clients
        self.get_status_client = self.create_client(GetStatus, 'get_robot_status')
        self.set_command_client = self.create_client(SetCommand, 'set_robot_command')

        # Wait for services
        self.get_logger().info('Waiting for services...')

        while not self.get_status_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('get_robot_status service not available, waiting...')

        while not self.set_command_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('set_robot_command service not available, waiting...')

        self.get_logger().info('Services available!')

    def get_status(self, robot_name: str):
        """Get status of a robot."""
        request = GetStatus.Request()
        request.robot_name = robot_name

        future = self.get_status_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()
        return response

    def send_command(self, robot_name: str, command_type: int, parameters: list = None):
        """Send command to a robot."""
        request = SetCommand.Request()
        request.robot_name = robot_name
        request.command_type = command_type
        request.parameters = parameters or []

        future = self.set_command_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()
        return response


def print_status(status: RobotStatus):
    """Pretty print robot status."""
    mode_names = {
        RobotStatus.MODE_MANUAL: 'MANUAL',
        RobotStatus.MODE_STABILIZE: 'STABILIZE',
        RobotStatus.MODE_DEPTH_HOLD: 'DEPTH_HOLD',
        RobotStatus.MODE_AUTO: 'AUTO'
    }

    print(f'\n=== Robot Status: {status.robot_name} ===')
    print(f'  ID: {status.robot_id}')
    print(f'  Position: ({status.position.x:.2f}, {status.position.y:.2f}, {status.position.z:.2f})')
    print(f'  Mode: {mode_names.get(status.mode, "UNKNOWN")}')
    print(f'  Armed: {status.is_armed}')
    print(f'  Connected: {status.is_connected}')
    print(f'  Battery: {status.battery_level:.1f}%')
    print()


def main(args=None):
    rclpy.init(args=args)
    client = ServiceClient()

    robot_name = 'bluerov2'

    try:
        # Get initial status
        print('\n--- Getting initial status ---')
        response = client.get_status(robot_name)
        if response.success:
            print_status(response.status)
        else:
            print(f'Error: {response.message}')

        # Arm the robot
        print('--- Arming robot ---')
        response = client.send_command(robot_name, SetCommand.Request.CMD_ARM)
        print(f'Result: {response.message} (Command ID: {response.command_id})')

        # Set mode to DEPTH_HOLD
        print('\n--- Setting mode to DEPTH_HOLD ---')
        response = client.send_command(
            robot_name,
            SetCommand.Request.CMD_SET_MODE,
            [float(RobotStatus.MODE_DEPTH_HOLD)]
        )
        print(f'Result: {response.message}')

        # Set target depth
        print('\n--- Setting target depth to 5m ---')
        response = client.send_command(
            robot_name,
            SetCommand.Request.CMD_SET_DEPTH,
            [5.0]
        )
        print(f'Result: {response.message}')

        # Get updated status
        print('\n--- Getting updated status ---')
        response = client.get_status(robot_name)
        if response.success:
            print_status(response.status)

        # Disarm
        print('--- Disarming robot ---')
        response = client.send_command(robot_name, SetCommand.Request.CMD_DISARM)
        print(f'Result: {response.message}')

    except KeyboardInterrupt:
        pass
    finally:
        client.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
