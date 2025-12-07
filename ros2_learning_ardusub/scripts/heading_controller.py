#!/usr/bin/env python3
"""
Heading Controller Node.
PID controller for heading/yaw hold.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Bool
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Wrench
import math
import time


class HeadingController(Node):
    """PID heading controller for underwater vehicles."""

    def __init__(self):
        super().__init__('heading_controller')

        # PID parameters
        self.declare_parameter('kp', 10.0)
        self.declare_parameter('ki', 1.0)
        self.declare_parameter('kd', 5.0)
        self.declare_parameter('max_torque', 20.0)
        self.declare_parameter('dead_band', 0.02)  # radians (~1 degree)
        self.declare_parameter('rate', 50.0)

        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        self.max_torque = self.get_parameter('max_torque').value
        self.dead_band = self.get_parameter('dead_band').value

        # State
        self.target_heading = 0.0  # radians
        self.current_heading = 0.0  # radians
        self.enabled = False

        # PID state
        self.integral = 0.0
        self.last_error = 0.0
        self.last_time = time.time()

        # Publishers
        self.torque_pub = self.create_publisher(Float64, 'heading/torque', 10)
        self.wrench_pub = self.create_publisher(Wrench, 'cmd_wrench', 10)
        self.error_pub = self.create_publisher(Float64, 'heading/error', 10)

        # Subscribers
        self.imu_sub = self.create_subscription(
            Imu, 'imu/data', self.imu_callback, 10
        )

        self.heading_sub = self.create_subscription(
            Float64, 'heading', self.heading_callback, 10
        )

        self.target_sub = self.create_subscription(
            Float64, 'heading/target', self.target_callback, 10
        )

        self.enable_sub = self.create_subscription(
            Bool, 'heading/enable', self.enable_callback, 10
        )

        # Control loop timer
        rate = self.get_parameter('rate').value
        self.timer = self.create_timer(1.0 / rate, self.control_loop)

        self.get_logger().info('Heading Controller initialized')

    def imu_callback(self, msg: Imu):
        """Extract heading from IMU quaternion."""
        q = msg.orientation
        # Calculate yaw from quaternion
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.current_heading = math.atan2(siny_cosp, cosy_cosp)

    def heading_callback(self, msg: Float64):
        """Update current heading (alternative input)."""
        self.current_heading = msg.data

    def target_callback(self, msg: Float64):
        """Update target heading."""
        self.target_heading = msg.data
        # Normalize to [-pi, pi]
        self.target_heading = self._normalize_angle(self.target_heading)
        self.get_logger().info(
            f'Target heading set to {math.degrees(self.target_heading):.1f}°'
        )
        self.integral = 0.0

    def enable_callback(self, msg: Bool):
        """Enable/disable controller."""
        self.enabled = msg.data
        if not self.enabled:
            self.integral = 0.0
        self.get_logger().info(
            f'Heading controller {"enabled" if self.enabled else "disabled"}'
        )

    def _normalize_angle(self, angle: float) -> float:
        """Normalize angle to [-pi, pi]."""
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle

    def _shortest_angular_distance(self, from_angle: float, to_angle: float) -> float:
        """Calculate shortest angular distance (handles wrap-around)."""
        diff = self._normalize_angle(to_angle - from_angle)
        return diff

    def control_loop(self):
        """PID control loop."""
        if not self.enabled:
            return

        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time

        if dt <= 0:
            return

        # Calculate error (shortest path)
        error = self._shortest_angular_distance(self.current_heading, self.target_heading)

        # Publish error
        error_msg = Float64()
        error_msg.data = error
        self.error_pub.publish(error_msg)

        # Dead band
        if abs(error) < self.dead_band:
            error = 0.0

        # Proportional term
        p_term = self.kp * error

        # Integral term
        self.integral += error * dt
        self.integral = max(-self.max_torque / self.ki,
                           min(self.max_torque / self.ki, self.integral))
        i_term = self.ki * self.integral

        # Derivative term
        derivative = self._shortest_angular_distance(self.last_error, error) / dt
        d_term = self.kd * derivative
        self.last_error = error

        # Calculate total torque
        torque = p_term + i_term + d_term
        torque = max(-self.max_torque, min(self.max_torque, torque))

        # Publish torque
        torque_msg = Float64()
        torque_msg.data = torque
        self.torque_pub.publish(torque_msg)

        # Publish as wrench
        wrench_msg = Wrench()
        wrench_msg.torque.z = torque
        self.wrench_pub.publish(wrench_msg)

        self.get_logger().debug(
            f'Heading: {math.degrees(self.current_heading):.1f}°, '
            f'Target: {math.degrees(self.target_heading):.1f}°, '
            f'Error: {math.degrees(error):.1f}°, '
            f'Torque: {torque:.2f}Nm'
        )


def main(args=None):
    rclpy.init(args=args)
    node = HeadingController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
