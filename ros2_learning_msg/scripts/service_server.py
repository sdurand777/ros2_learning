#!/usr/bin/env python3
"""
Example service server using custom services.
Provides GetStatus and SetCommand services.
"""

import rclpy
from rclpy.node import Node
from ros2_learning_msg.srv import GetStatus, SetCommand
from ros2_learning_msg.msg import RobotStatus
from geometry_msgs.msg import Point, Quaternion, Twist, Vector3
from std_msgs.msg import Header
import random


class ServiceServer(Node):
    def __init__(self):
        super().__init__('service_server')

        # Services
        self.get_status_srv = self.create_service(
            GetStatus,
            'get_robot_status',
            self.get_status_callback
        )

        self.set_command_srv = self.create_service(
            SetCommand,
            'set_robot_command',
            self.set_command_callback
        )

        # Robot state
        self.robots = {
            'bluerov2': {
                'id': 1,
                'armed': False,
                'mode': RobotStatus.MODE_MANUAL,
                'depth': 0.0,
                'heading': 0.0,
                'battery': 95.0
            },
            'bluerov2_heavy': {
                'id': 2,
                'armed': False,
                'mode': RobotStatus.MODE_MANUAL,
                'depth': 0.0,
                'heading': 0.0,
                'battery': 87.0
            }
        }

        self.command_counter = 0

        self.get_logger().info('Service Server initialized')
        self.get_logger().info(f'Available robots: {list(self.robots.keys())}')

    def get_status_callback(self, request, response):
        robot_name = request.robot_name

        if robot_name not in self.robots:
            response.success = False
            response.message = f'Robot "{robot_name}" not found'
            response.status = RobotStatus()
            self.get_logger().warn(f'Status request for unknown robot: {robot_name}')
            return response

        robot = self.robots[robot_name]

        # Build status message
        status = RobotStatus()
        status.header = Header()
        status.header.stamp = self.get_clock().now().to_msg()
        status.header.frame_id = 'world'

        status.robot_name = robot_name
        status.robot_id = robot['id']

        status.position = Point(
            x=random.uniform(-10, 10),
            y=random.uniform(-10, 10),
            z=-robot['depth']
        )

        status.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        status.velocity = Twist()

        status.battery_level = robot['battery']
        status.is_armed = robot['armed']
        status.is_connected = True
        status.mode = robot['mode']

        response.success = True
        response.message = 'Status retrieved successfully'
        response.status = status

        self.get_logger().info(f'Status request for {robot_name}: OK')
        return response

    def set_command_callback(self, request, response):
        robot_name = request.robot_name
        cmd_type = request.command_type
        params = list(request.parameters)

        if robot_name not in self.robots:
            response.success = False
            response.message = f'Robot "{robot_name}" not found'
            response.command_id = 0
            return response

        robot = self.robots[robot_name]
        self.command_counter += 1

        # Process command
        cmd_names = {
            SetCommand.Request.CMD_ARM: 'ARM',
            SetCommand.Request.CMD_DISARM: 'DISARM',
            SetCommand.Request.CMD_SET_MODE: 'SET_MODE',
            SetCommand.Request.CMD_SET_DEPTH: 'SET_DEPTH',
            SetCommand.Request.CMD_SET_HEADING: 'SET_HEADING',
            SetCommand.Request.CMD_MOVE: 'MOVE'
        }

        cmd_name = cmd_names.get(cmd_type, 'UNKNOWN')

        if cmd_type == SetCommand.Request.CMD_ARM:
            robot['armed'] = True
            msg = 'Robot armed'
        elif cmd_type == SetCommand.Request.CMD_DISARM:
            robot['armed'] = False
            msg = 'Robot disarmed'
        elif cmd_type == SetCommand.Request.CMD_SET_MODE:
            if params:
                robot['mode'] = int(params[0])
                msg = f'Mode set to {int(params[0])}'
            else:
                msg = 'No mode specified'
        elif cmd_type == SetCommand.Request.CMD_SET_DEPTH:
            if params:
                robot['depth'] = params[0]
                msg = f'Target depth set to {params[0]}m'
            else:
                msg = 'No depth specified'
        elif cmd_type == SetCommand.Request.CMD_SET_HEADING:
            if params:
                robot['heading'] = params[0]
                msg = f'Target heading set to {params[0]}°'
            else:
                msg = 'No heading specified'
        elif cmd_type == SetCommand.Request.CMD_MOVE:
            msg = f'Move command received with {len(params)} parameters'
        else:
            response.success = False
            response.message = f'Unknown command type: {cmd_type}'
            response.command_id = self.command_counter
            return response

        response.success = True
        response.message = msg
        response.command_id = self.command_counter

        self.get_logger().info(
            f'Command {cmd_name} for {robot_name}: {msg} (ID: {self.command_counter})'
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ServiceServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
