#!/usr/bin/env python3
"""
Pose Publisher Node.
Subscribes to Gazebo pose topics and republishes as ROS2 messages.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, TransformStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
import math


class PosePublisher(Node):
    def __init__(self):
        super().__init__('pose_publisher')

        # Declare parameters
        self.declare_parameter('robot_name', 'bluerov2')
        self.declare_parameter('world_frame', 'world')
        self.declare_parameter('base_frame', 'base_link')
        self.declare_parameter('publish_tf', True)

        self.robot_name = self.get_parameter('robot_name').value
        self.world_frame = self.get_parameter('world_frame').value
        self.base_frame = self.get_parameter('base_frame').value
        self.publish_tf = self.get_parameter('publish_tf').value

        # TF broadcaster
        if self.publish_tf:
            self.tf_broadcaster = TransformBroadcaster(self)

        # Publishers
        self.pose_pub = self.create_publisher(
            PoseStamped,
            f'{self.robot_name}/pose',
            10
        )

        # Subscriber from Gazebo (via bridge)
        self.odom_sub = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10
        )

        # State
        self.last_pose = None
        self.message_count = 0

        self.get_logger().info(f'Pose Publisher initialized for {self.robot_name}')

    def odom_callback(self, msg: Odometry):
        """Process odometry from Gazebo and publish pose + TF."""
        self.message_count += 1

        # Create PoseStamped
        pose_msg = PoseStamped()
        pose_msg.header.stamp = msg.header.stamp
        pose_msg.header.frame_id = self.world_frame
        pose_msg.pose = msg.pose.pose

        self.pose_pub.publish(pose_msg)
        self.last_pose = pose_msg

        # Broadcast TF
        if self.publish_tf:
            t = TransformStamped()
            t.header.stamp = msg.header.stamp
            t.header.frame_id = self.world_frame
            t.child_frame_id = f'{self.robot_name}/{self.base_frame}'

            t.transform.translation.x = msg.pose.pose.position.x
            t.transform.translation.y = msg.pose.pose.position.y
            t.transform.translation.z = msg.pose.pose.position.z
            t.transform.rotation = msg.pose.pose.orientation

            self.tf_broadcaster.sendTransform(t)

        # Log periodically
        if self.message_count % 100 == 0:
            pos = msg.pose.pose.position
            self.get_logger().info(
                f'Pose #{self.message_count}: '
                f'({pos.x:.2f}, {pos.y:.2f}, {pos.z:.2f})'
            )

    def get_euler_from_quaternion(self, q) -> tuple:
        """Convert quaternion to Euler angles (roll, pitch, yaw)."""
        # Roll (x-axis rotation)
        sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
        cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
        roll = math.atan2(sinr_cosp, cosr_cosp)

        # Pitch (y-axis rotation)
        sinp = 2 * (q.w * q.y - q.z * q.x)
        if abs(sinp) >= 1:
            pitch = math.copysign(math.pi / 2, sinp)
        else:
            pitch = math.asin(sinp)

        # Yaw (z-axis rotation)
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw


def main(args=None):
    rclpy.init(args=args)
    node = PosePublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
