#!/usr/bin/env python3
"""
Gazebo Model Spawner.
Spawns models in Gazebo Harmonic simulation using gz service calls.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose, Point, Quaternion
import subprocess
import os
import math


class ModelSpawner(Node):
    def __init__(self):
        super().__init__('model_spawner')

        # Declare parameters
        self.declare_parameter('world_name', 'underwater_world')
        self.declare_parameter('model_name', 'bluerov2')
        self.declare_parameter('model_sdf', '')
        self.declare_parameter('x', 0.0)
        self.declare_parameter('y', 0.0)
        self.declare_parameter('z', -1.0)
        self.declare_parameter('roll', 0.0)
        self.declare_parameter('pitch', 0.0)
        self.declare_parameter('yaw', 0.0)

        self.world_name = self.get_parameter('world_name').value
        self.model_name = self.get_parameter('model_name').value
        self.model_sdf = self.get_parameter('model_sdf').value

        self.initial_pose = Pose()
        self.initial_pose.position = Point(
            x=self.get_parameter('x').value,
            y=self.get_parameter('y').value,
            z=self.get_parameter('z').value
        )

        # Convert Euler to Quaternion
        roll = self.get_parameter('roll').value
        pitch = self.get_parameter('pitch').value
        yaw = self.get_parameter('yaw').value
        self.initial_pose.orientation = self._euler_to_quaternion(roll, pitch, yaw)

        self.get_logger().info(f'Model Spawner initialized')
        self.get_logger().info(f'World: {self.world_name}')

    def _euler_to_quaternion(self, roll: float, pitch: float, yaw: float) -> Quaternion:
        """Convert Euler angles to Quaternion."""
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        q = Quaternion()
        q.w = cr * cp * cy + sr * sp * sy
        q.x = sr * cp * cy - cr * sp * sy
        q.y = cr * sp * cy + sr * cp * sy
        q.z = cr * cp * sy - sr * sp * cy
        return q

    def spawn_model(self, model_name: str = None, sdf_string: str = None,
                    pose: Pose = None) -> bool:
        """
        Spawn a model in Gazebo using gz service.

        Args:
            model_name: Name of the model in simulation
            sdf_string: SDF XML string (or use model_sdf parameter)
            pose: Initial pose (or use parameter values)

        Returns:
            bool: True if successful
        """
        name = model_name or self.model_name
        p = pose or self.initial_pose

        # Use provided SDF or load from parameter/file
        if sdf_string is None:
            sdf_string = self.model_sdf or self._get_default_box_sdf(name)

        # Build gz service command
        cmd = [
            'gz', 'service',
            '-s', f'/world/{self.world_name}/create',
            '--reqtype', 'gz.msgs.EntityFactory',
            '--reptype', 'gz.msgs.Boolean',
            '--timeout', '5000',
            '--req',
            f'sdf: "{sdf_string}" '
            f'name: "{name}" '
            f'pose: {{'
            f'position: {{x: {p.position.x}, y: {p.position.y}, z: {p.position.z}}} '
            f'orientation: {{x: {p.orientation.x}, y: {p.orientation.y}, '
            f'z: {p.orientation.z}, w: {p.orientation.w}}}'
            f'}}'
        ]

        self.get_logger().info(f'Spawning model: {name}')
        self.get_logger().debug(f'Command: {" ".join(cmd)}')

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.get_logger().info(f'Model {name} spawned successfully')
                return True
            else:
                self.get_logger().error(f'Failed to spawn model: {result.stderr}')
                return False
        except subprocess.TimeoutExpired:
            self.get_logger().error('Spawn command timed out')
            return False
        except Exception as e:
            self.get_logger().error(f'Error spawning model: {e}')
            return False

    def delete_model(self, model_name: str) -> bool:
        """Delete a model from Gazebo."""
        cmd = [
            'gz', 'service',
            '-s', f'/world/{self.world_name}/remove',
            '--reqtype', 'gz.msgs.Entity',
            '--reptype', 'gz.msgs.Boolean',
            '--timeout', '5000',
            '--req', f'name: "{model_name}" type: MODEL'
        ]

        self.get_logger().info(f'Deleting model: {model_name}')

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.get_logger().info(f'Model {model_name} deleted')
                return True
            else:
                self.get_logger().error(f'Failed to delete model: {result.stderr}')
                return False
        except Exception as e:
            self.get_logger().error(f'Error deleting model: {e}')
            return False

    def _get_default_box_sdf(self, name: str) -> str:
        """Return a simple box SDF for testing."""
        return f'''<?xml version="1.0"?>
<sdf version="1.8">
  <model name="{name}">
    <static>false</static>
    <link name="base_link">
      <inertial>
        <mass>10.0</mass>
        <inertia>
          <ixx>0.1</ixx><iyy>0.1</iyy><izz>0.1</izz>
        </inertia>
      </inertial>
      <collision name="collision">
        <geometry>
          <box><size>0.5 0.3 0.2</size></box>
        </geometry>
      </collision>
      <visual name="visual">
        <geometry>
          <box><size>0.5 0.3 0.2</size></box>
        </geometry>
        <material>
          <ambient>0.0 0.0 1.0 1</ambient>
          <diffuse>0.0 0.0 0.8 1</diffuse>
        </material>
      </visual>
    </link>
  </model>
</sdf>'''


def main(args=None):
    rclpy.init(args=args)
    node = ModelSpawner()

    # Spawn a test model
    node.spawn_model()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
