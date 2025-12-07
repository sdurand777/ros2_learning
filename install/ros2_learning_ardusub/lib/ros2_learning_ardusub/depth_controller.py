#!/usr/bin/env python3
"""
Depth Controller Node.
PID controller for depth hold mode.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Bool
from geometry_msgs.msg import Wrench
import time


class DepthController(Node):
    """PID depth controller for underwater vehicles."""

    def __init__(self):
        super().__init__('depth_controller')

        # PID parameters
        self.declare_parameter('kp', 50.0)
        self.declare_parameter('ki', 5.0)
        self.declare_parameter('kd', 20.0)
        self.declare_parameter('max_thrust', 100.0)
        self.declare_parameter('dead_band', 0.05)
        self.declare_parameter('rate', 50.0)

        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        self.max_thrust = self.get_parameter('max_thrust').value
        self.dead_band = self.get_parameter('dead_band').value

        # State
        self.target_depth = 0.0
        self.current_depth = 0.0
        self.enabled = False

        # PID state
        self.integral = 0.0
        self.last_error = 0.0
        self.last_time = time.time()

        # Publishers
        self.thrust_pub = self.create_publisher(Float64, 'depth/thrust', 10)
        self.wrench_pub = self.create_publisher(Wrench, 'cmd_wrench', 10)
        self.error_pub = self.create_publisher(Float64, 'depth/error', 10)

        # Subscribers
        self.depth_sub = self.create_subscription(
            Float64, 'depth', self.depth_callback, 10
        )

        self.target_sub = self.create_subscription(
            Float64, 'depth/target', self.target_callback, 10
        )

        self.enable_sub = self.create_subscription(
            Bool, 'depth/enable', self.enable_callback, 10
        )

        # Control loop timer
        rate = self.get_parameter('rate').value
        self.timer = self.create_timer(1.0 / rate, self.control_loop)

        self.get_logger().info('Depth Controller initialized')
        self.get_logger().info(f'PID gains: Kp={self.kp}, Ki={self.ki}, Kd={self.kd}')

    def depth_callback(self, msg: Float64):
        """Update current depth."""
        self.current_depth = msg.data

    def target_callback(self, msg: Float64):
        """Update target depth."""
        self.target_depth = msg.data
        self.get_logger().info(f'Target depth set to {self.target_depth:.2f}m')

        # Reset integral when target changes
        self.integral = 0.0

    def enable_callback(self, msg: Bool):
        """Enable/disable controller."""
        self.enabled = msg.data
        if not self.enabled:
            self.integral = 0.0
        self.get_logger().info(f'Depth controller {"enabled" if self.enabled else "disabled"}')

    def control_loop(self):
        """PID control loop."""
        if not self.enabled:
            return

        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time

        if dt <= 0:
            return

        # Calculate error (positive error = need to go deeper)
        error = self.target_depth - self.current_depth

        # Publish error for debugging
        error_msg = Float64()
        error_msg.data = error
        self.error_pub.publish(error_msg)

        # Dead band
        if abs(error) < self.dead_band:
            error = 0.0

        # Proportional term
        p_term = self.kp * error

        # Integral term (with anti-windup)
        self.integral += error * dt
        self.integral = max(-self.max_thrust / self.ki,
                           min(self.max_thrust / self.ki, self.integral))
        i_term = self.ki * self.integral

        # Derivative term
        derivative = (error - self.last_error) / dt
        d_term = self.kd * derivative
        self.last_error = error

        # Calculate total thrust
        thrust = p_term + i_term + d_term

        # Clamp thrust
        thrust = max(-self.max_thrust, min(self.max_thrust, thrust))

        # Publish thrust
        thrust_msg = Float64()
        thrust_msg.data = thrust
        self.thrust_pub.publish(thrust_msg)

        # Publish as wrench (vertical force only)
        wrench_msg = Wrench()
        wrench_msg.force.z = -thrust  # Negative because depth is positive downward
        self.wrench_pub.publish(wrench_msg)

        self.get_logger().debug(
            f'Depth: {self.current_depth:.2f}m, Target: {self.target_depth:.2f}m, '
            f'Error: {error:.2f}m, Thrust: {thrust:.1f}N'
        )


def main(args=None):
    rclpy.init(args=args)
    node = DepthController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
