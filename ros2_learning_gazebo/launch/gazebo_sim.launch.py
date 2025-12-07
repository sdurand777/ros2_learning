#!/usr/bin/env python3
"""
Launch file for Gazebo Harmonic simulation with ROS2 bridge.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    # Declare arguments
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='underwater_world',
        description='Name of the Gazebo world'
    )

    robot_name_arg = DeclareLaunchArgument(
        'robot_name',
        default_value='bluerov2',
        description='Name of the robot'
    )

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation time'
    )

    headless_arg = DeclareLaunchArgument(
        'headless',
        default_value='false',
        description='Run Gazebo in headless mode'
    )

    # Get configurations
    world = LaunchConfiguration('world')
    robot_name = LaunchConfiguration('robot_name')
    use_sim_time = LaunchConfiguration('use_sim_time')
    headless = LaunchConfiguration('headless')

    # Package share directory
    pkg_share = FindPackageShare('ros2_learning_gazebo')

    # Start Gazebo
    gz_sim = ExecuteProcess(
        cmd=[
            'gz', 'sim', '-r',
            PathJoinSubstitution([pkg_share, 'config', 'worlds', 'underwater.sdf'])
        ],
        output='screen'
    )

    # ROS-Gazebo Bridge for common topics
    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/model/bluerov2/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/model/bluerov2/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
        ],
        output='screen'
    )

    # Pose publisher node
    pose_publisher = Node(
        package='ros2_learning_gazebo',
        executable='pose_publisher.py',
        name='pose_publisher',
        parameters=[{
            'robot_name': robot_name,
            'use_sim_time': use_sim_time
        }],
        output='screen'
    )

    # Sensor reader node
    sensor_reader = Node(
        package='ros2_learning_gazebo',
        executable='sensor_reader.py',
        name='sensor_reader',
        parameters=[{
            'robot_name': robot_name,
            'use_sim_time': use_sim_time,
            'log_rate': 1.0
        }],
        output='screen'
    )

    return LaunchDescription([
        world_arg,
        robot_name_arg,
        use_sim_time_arg,
        headless_arg,
        gz_sim,
        bridge_node,
        pose_publisher,
        sensor_reader,
    ])
