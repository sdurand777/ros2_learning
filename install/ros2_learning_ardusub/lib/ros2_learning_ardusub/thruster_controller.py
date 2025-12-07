#!/usr/bin/env python3
"""
Thruster Controller Node.
Controls BlueROV2 thrusters via PWM commands.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Wrench
from std_msgs.msg import Float64MultiArray, UInt16MultiArray
import numpy as np


class ThrusterController(Node):
    """
    Thruster controller for BlueROV2.

    BlueROV2 Heavy has 8 thrusters:
    - 4 horizontal (vectored)
    - 4 vertical

    This controller converts Twist commands to individual thruster PWM values.
    """

    # Thruster configuration for BlueROV2 Heavy
    # Position: [x, y, z] relative to center
    # Direction: [fx, fy, fz] force direction when positive thrust
    THRUSTER_CONFIG = {
        0: {'pos': [0.14, 0.10, 0.0], 'dir': [0.707, -0.707, 0.0]},   # Front-right
        1: {'pos': [0.14, -0.10, 0.0], 'dir': [0.707, 0.707, 0.0]},   # Front-left
        2: {'pos': [-0.14, 0.10, 0.0], 'dir': [0.707, 0.707, 0.0]},   # Rear-right
        3: {'pos': [-0.14, -0.10, 0.0], 'dir': [0.707, -0.707, 0.0]}, # Rear-left
        4: {'pos': [0.12, 0.22, 0.0], 'dir': [0.0, 0.0, 1.0]},        # Vertical front-right
        5: {'pos': [0.12, -0.22, 0.0], 'dir': [0.0, 0.0, 1.0]},       # Vertical front-left
        6: {'pos': [-0.12, 0.22, 0.0], 'dir': [0.0, 0.0, 1.0]},       # Vertical rear-right
        7: {'pos': [-0.12, -0.22, 0.0], 'dir': [0.0, 0.0, 1.0]},      # Vertical rear-left
    }

    # PWM values
    PWM_NEUTRAL = 1500
    PWM_MIN = 1100
    PWM_MAX = 1900

    def __init__(self):
        super().__init__('thruster_controller')

        # Parameters
        self.declare_parameter('max_thrust', 40.0)  # Newtons per thruster
        self.declare_parameter('vehicle_mass', 11.5)  # kg

        self.max_thrust = self.get_parameter('max_thrust').value

        # Build thrust allocation matrix
        self.thrust_matrix = self._build_thrust_matrix()

        # Publishers
        self.pwm_pub = self.create_publisher(UInt16MultiArray, 'thrusters/pwm', 10)
        self.thrust_pub = self.create_publisher(Float64MultiArray, 'thrusters/thrust', 10)

        # Subscribers
        self.cmd_vel_sub = self.create_subscription(
            Twist, 'cmd_vel', self.cmd_vel_callback, 10
        )

        self.wrench_sub = self.create_subscription(
            Wrench, 'cmd_wrench', self.wrench_callback, 10
        )

        self.get_logger().info('Thruster Controller initialized')
        self.get_logger().info(f'Thrust matrix shape: {self.thrust_matrix.shape}')

    def _build_thrust_matrix(self) -> np.ndarray:
        """
        Build the thrust allocation matrix.

        Maps [Fx, Fy, Fz, Tx, Ty, Tz] to [T0, T1, ..., T7] thruster forces.
        """
        n_thrusters = len(self.THRUSTER_CONFIG)
        B = np.zeros((6, n_thrusters))

        for i, config in self.THRUSTER_CONFIG.items():
            pos = np.array(config['pos'])
            direction = np.array(config['dir'])

            # Force contribution
            B[0:3, i] = direction

            # Torque contribution (r x F)
            B[3:6, i] = np.cross(pos, direction)

        return B

    def _allocate_thrust(self, wrench: np.ndarray) -> np.ndarray:
        """
        Allocate thrust to individual thrusters using pseudo-inverse.

        Args:
            wrench: [Fx, Fy, Fz, Tx, Ty, Tz] desired forces/torques

        Returns:
            Array of thruster forces
        """
        # Use pseudo-inverse for thrust allocation
        B_pinv = np.linalg.pinv(self.thrust_matrix)
        thrusts = B_pinv @ wrench

        # Clamp to max thrust
        thrusts = np.clip(thrusts, -self.max_thrust, self.max_thrust)

        return thrusts

    def _thrust_to_pwm(self, thrust: float) -> int:
        """Convert thrust (Newtons) to PWM value."""
        # Normalize thrust to -1 to 1
        normalized = thrust / self.max_thrust

        # Convert to PWM (linear approximation)
        pwm = int(self.PWM_NEUTRAL + normalized * (self.PWM_MAX - self.PWM_NEUTRAL))

        return max(self.PWM_MIN, min(self.PWM_MAX, pwm))

    def cmd_vel_callback(self, msg: Twist):
        """Convert Twist to wrench and allocate thrust."""
        # Simple mapping from velocity command to force command
        # In reality, this would use a velocity controller
        mass = self.get_parameter('vehicle_mass').value

        wrench = np.array([
            msg.linear.x * mass * 2.0,   # Fx (forward)
            msg.linear.y * mass * 2.0,   # Fy (lateral)
            msg.linear.z * mass * 2.0,   # Fz (vertical)
            msg.angular.x * 0.5,          # Tx (roll)
            msg.angular.y * 0.5,          # Ty (pitch)
            msg.angular.z * mass * 1.0,   # Tz (yaw)
        ])

        self._process_wrench(wrench)

    def wrench_callback(self, msg: Wrench):
        """Direct wrench command."""
        wrench = np.array([
            msg.force.x,
            msg.force.y,
            msg.force.z,
            msg.torque.x,
            msg.torque.y,
            msg.torque.z,
        ])

        self._process_wrench(wrench)

    def _process_wrench(self, wrench: np.ndarray):
        """Process wrench command and publish thruster outputs."""
        # Allocate thrust
        thrusts = self._allocate_thrust(wrench)

        # Convert to PWM
        pwm_values = [self._thrust_to_pwm(t) for t in thrusts]

        # Publish thrust values
        thrust_msg = Float64MultiArray()
        thrust_msg.data = thrusts.tolist()
        self.thrust_pub.publish(thrust_msg)

        # Publish PWM values
        pwm_msg = UInt16MultiArray()
        pwm_msg.data = pwm_values
        self.pwm_pub.publish(pwm_msg)

        self.get_logger().debug(
            f'Thrust: {[f"{t:.1f}" for t in thrusts]} N, '
            f'PWM: {pwm_values}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ThrusterController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
