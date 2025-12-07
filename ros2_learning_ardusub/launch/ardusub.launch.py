#!/usr/bin/env python3
"""
Launch file for ArduSub ROS2 nodes.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Declare arguments
    connection_arg = DeclareLaunchArgument(
        'connection',
        default_value='udpin:0.0.0.0:14550',
        description='MAVLink connection string'
    )

    simulation_arg = DeclareLaunchArgument(
        'simulation',
        default_value='true',
        description='Run in simulation mode (no real hardware)'
    )

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation time'
    )

    enable_depth_ctrl_arg = DeclareLaunchArgument(
        'enable_depth_control',
        default_value='true',
        description='Enable depth controller'
    )

    enable_heading_ctrl_arg = DeclareLaunchArgument(
        'enable_heading_control',
        default_value='true',
        description='Enable heading controller'
    )

    # Get configurations
    connection = LaunchConfiguration('connection')
    simulation = LaunchConfiguration('simulation')
    use_sim_time = LaunchConfiguration('use_sim_time')
    enable_depth = LaunchConfiguration('enable_depth_control')
    enable_heading = LaunchConfiguration('enable_heading_control')

    pkg_share = FindPackageShare('ros2_learning_ardusub')

    # Nodes
    ardusub_node = Node(
        package='ros2_learning_ardusub',
        executable='ardusub_node.py',
        name='ardusub',
        parameters=[{
            'connection_string': connection,
            'use_sim_time': use_sim_time
        }],
        output='screen'
    )

    telemetry_node = Node(
        package='ros2_learning_ardusub',
        executable='telemetry_publisher.py',
        name='telemetry_publisher',
        condition=IfCondition(simulation),
        parameters=[{
            'rate': 50.0,
            'use_sim_time': use_sim_time
        }],
        output='screen'
    )

    thruster_node = Node(
        package='ros2_learning_ardusub',
        executable='thruster_controller.py',
        name='thruster_controller',
        parameters=[{
            'max_thrust': 40.0,
            'use_sim_time': use_sim_time
        }],
        output='screen'
    )

    depth_node = Node(
        package='ros2_learning_ardusub',
        executable='depth_controller.py',
        name='depth_controller',
        condition=IfCondition(enable_depth),
        parameters=[
            PathJoinSubstitution([pkg_share, 'config', 'depth_controller.yaml']),
            {'use_sim_time': use_sim_time}
        ],
        output='screen'
    )

    heading_node = Node(
        package='ros2_learning_ardusub',
        executable='heading_controller.py',
        name='heading_controller',
        condition=IfCondition(enable_heading),
        parameters=[
            PathJoinSubstitution([pkg_share, 'config', 'heading_controller.yaml']),
            {'use_sim_time': use_sim_time}
        ],
        output='screen'
    )

    return LaunchDescription([
        connection_arg,
        simulation_arg,
        use_sim_time_arg,
        enable_depth_ctrl_arg,
        enable_heading_ctrl_arg,
        ardusub_node,
        telemetry_node,
        thruster_node,
        depth_node,
        heading_node,
    ])
