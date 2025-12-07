#!/usr/bin/env python3
"""
Gazebo Harmonic Bridge Node.
Creates a ROS2 node that interfaces with Gazebo via ros_gz_bridge.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose, PoseStamped
from sensor_msgs.msg import Imu, LaserScan, Image, CameraInfo
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64, String
import subprocess
import os


class GazeboBridgeNode(Node):
    def __init__(self):
        super().__init__('gazebo_bridge_node')

        # Declare parameters
        self.declare_parameter('world_name', 'underwater_world')
        self.declare_parameter('robot_name', 'bluerov2')
        self.declare_parameter('use_sim_time', True)

        self.world_name = self.get_parameter('world_name').value
        self.robot_name = self.get_parameter('robot_name').value

        # Publishers (from Gazebo to ROS2)
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)
        self.imu_pub = self.create_publisher(Imu, 'imu/data', 10)
        self.pose_pub = self.create_publisher(PoseStamped, 'pose', 10)

        # Subscribers (from ROS2 to Gazebo)
        self.cmd_vel_sub = self.create_subscription(
            Twist, 'cmd_vel', self.cmd_vel_callback, 10
        )

        # Bridge topics configuration
        self.bridge_topics = self._get_bridge_topics()

        self.get_logger().info(f'Gazebo Bridge Node initialized')
        self.get_logger().info(f'World: {self.world_name}, Robot: {self.robot_name}')
        self.get_logger().info('Bridge topics configured')

    def _get_bridge_topics(self) -> list:
        """Return list of topics to bridge between Gazebo and ROS2."""
        robot = self.robot_name
        return [
            # Gazebo -> ROS2
            {
                'gz_topic': f'/model/{robot}/odometry',
                'ros_topic': 'odom',
                'msg_type': 'nav_msgs/msg/Odometry',
                'direction': 'gz_to_ros'
            },
            {
                'gz_topic': f'/world/{self.world_name}/model/{robot}/link/base_link/sensor/imu/imu',
                'ros_topic': 'imu/data',
                'msg_type': 'sensor_msgs/msg/Imu',
                'direction': 'gz_to_ros'
            },
            {
                'gz_topic': f'/model/{robot}/pose',
                'ros_topic': 'pose',
                'msg_type': 'geometry_msgs/msg/PoseStamped',
                'direction': 'gz_to_ros'
            },
            # ROS2 -> Gazebo
            {
                'gz_topic': f'/model/{robot}/cmd_vel',
                'ros_topic': 'cmd_vel',
                'msg_type': 'geometry_msgs/msg/Twist',
                'direction': 'ros_to_gz'
            },
            {
                'gz_topic': f'/{robot}/thruster/0/cmd_thrust',
                'ros_topic': 'thrusters/0/cmd',
                'msg_type': 'std_msgs/msg/Float64',
                'direction': 'ros_to_gz'
            },
        ]

    def cmd_vel_callback(self, msg: Twist):
        """Handle velocity commands."""
        self.get_logger().debug(
            f'Cmd vel: linear=({msg.linear.x:.2f}, {msg.linear.y:.2f}, {msg.linear.z:.2f}), '
            f'angular=({msg.angular.x:.2f}, {msg.angular.y:.2f}, {msg.angular.z:.2f})'
        )

    def get_bridge_config_yaml(self) -> str:
        """Generate YAML configuration for ros_gz_bridge."""
        lines = []
        for topic in self.bridge_topics:
            if topic['direction'] == 'gz_to_ros':
                lines.append(f"- topic_name: \"{topic['ros_topic']}\"")
                lines.append(f"  ros_type_name: \"{topic['msg_type']}\"")
                lines.append(f"  gz_topic_name: \"{topic['gz_topic']}\"")
                lines.append("  direction: GZ_TO_ROS")
            else:
                lines.append(f"- topic_name: \"{topic['ros_topic']}\"")
                lines.append(f"  ros_type_name: \"{topic['msg_type']}\"")
                lines.append(f"  gz_topic_name: \"{topic['gz_topic']}\"")
                lines.append("  direction: ROS_TO_GZ")
            lines.append("")
        return '\n'.join(lines)

    def print_bridge_commands(self):
        """Print commands to manually start the bridge."""
        self.get_logger().info('=' * 60)
        self.get_logger().info('To start Gazebo bridge, run:')
        for topic in self.bridge_topics:
            direction = 'GzToRos' if topic['direction'] == 'gz_to_ros' else 'RosToGz'
            cmd = (
                f"ros2 run ros_gz_bridge parameter_bridge "
                f"{topic['gz_topic']}@{topic['msg_type']}@{direction}"
            )
            self.get_logger().info(cmd)
        self.get_logger().info('=' * 60)


def main(args=None):
    rclpy.init(args=args)
    node = GazeboBridgeNode()

    # Print bridge commands for reference
    node.print_bridge_commands()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
