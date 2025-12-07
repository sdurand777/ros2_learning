#!/usr/bin/env python3
"""
Velocity Controller Node.
Provides a simple interface to control robot velocity in Gazebo.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray
import sys
import termios
import tty
import select


class VelocityController(Node):
    def __init__(self):
        super().__init__('velocity_controller')

        # Declare parameters
        self.declare_parameter('max_linear_vel', 1.0)
        self.declare_parameter('max_angular_vel', 1.0)
        self.declare_parameter('linear_step', 0.1)
        self.declare_parameter('angular_step', 0.1)

        self.max_linear = self.get_parameter('max_linear_vel').value
        self.max_angular = self.get_parameter('max_angular_vel').value
        self.linear_step = self.get_parameter('linear_step').value
        self.angular_step = self.get_parameter('angular_step').value

        # Publisher
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        # Current velocity
        self.current_vel = Twist()

        # Timer for continuous publishing
        self.timer = self.create_timer(0.1, self.publish_velocity)

        self.get_logger().info('Velocity Controller initialized')
        self.print_controls()

    def print_controls(self):
        """Print keyboard controls."""
        msg = """
Velocity Controller - Keyboard Controls
----------------------------------------
Moving:
  w/s : increase/decrease linear X (forward/backward)
  a/d : increase/decrease linear Y (left/right)
  q/e : increase/decrease linear Z (up/down)

Rotation:
  j/l : increase/decrease angular Z (yaw)
  i/k : increase/decrease angular Y (pitch)
  u/o : increase/decrease angular X (roll)

Other:
  Space : stop all motion
  Ctrl+C : quit
----------------------------------------
"""
        self.get_logger().info(msg)

    def set_velocity(self, linear_x=None, linear_y=None, linear_z=None,
                     angular_x=None, angular_y=None, angular_z=None):
        """Set velocity components."""
        if linear_x is not None:
            self.current_vel.linear.x = self._clamp(linear_x, -self.max_linear, self.max_linear)
        if linear_y is not None:
            self.current_vel.linear.y = self._clamp(linear_y, -self.max_linear, self.max_linear)
        if linear_z is not None:
            self.current_vel.linear.z = self._clamp(linear_z, -self.max_linear, self.max_linear)
        if angular_x is not None:
            self.current_vel.angular.x = self._clamp(angular_x, -self.max_angular, self.max_angular)
        if angular_y is not None:
            self.current_vel.angular.y = self._clamp(angular_y, -self.max_angular, self.max_angular)
        if angular_z is not None:
            self.current_vel.angular.z = self._clamp(angular_z, -self.max_angular, self.max_angular)

    def stop(self):
        """Stop all motion."""
        self.current_vel = Twist()
        self.get_logger().info('STOP - All velocities set to zero')

    def _clamp(self, value: float, min_val: float, max_val: float) -> float:
        """Clamp value between min and max."""
        return max(min_val, min(max_val, value))

    def publish_velocity(self):
        """Publish current velocity."""
        self.cmd_vel_pub.publish(self.current_vel)

    def process_key(self, key: str):
        """Process keyboard input."""
        vel = self.current_vel

        if key == 'w':
            self.set_velocity(linear_x=vel.linear.x + self.linear_step)
        elif key == 's':
            self.set_velocity(linear_x=vel.linear.x - self.linear_step)
        elif key == 'a':
            self.set_velocity(linear_y=vel.linear.y + self.linear_step)
        elif key == 'd':
            self.set_velocity(linear_y=vel.linear.y - self.linear_step)
        elif key == 'q':
            self.set_velocity(linear_z=vel.linear.z + self.linear_step)
        elif key == 'e':
            self.set_velocity(linear_z=vel.linear.z - self.linear_step)
        elif key == 'j':
            self.set_velocity(angular_z=vel.angular.z + self.angular_step)
        elif key == 'l':
            self.set_velocity(angular_z=vel.angular.z - self.angular_step)
        elif key == 'i':
            self.set_velocity(angular_y=vel.angular.y + self.angular_step)
        elif key == 'k':
            self.set_velocity(angular_y=vel.angular.y - self.angular_step)
        elif key == 'u':
            self.set_velocity(angular_x=vel.angular.x + self.angular_step)
        elif key == 'o':
            self.set_velocity(angular_x=vel.angular.x - self.angular_step)
        elif key == ' ':
            self.stop()

        self.get_logger().debug(
            f'Vel: linear=({vel.linear.x:.2f}, {vel.linear.y:.2f}, {vel.linear.z:.2f}) '
            f'angular=({vel.angular.x:.2f}, {vel.angular.y:.2f}, {vel.angular.z:.2f})'
        )


def get_key(timeout=0.1):
    """Get keyboard input (non-blocking)."""
    if select.select([sys.stdin], [], [], timeout)[0]:
        return sys.stdin.read(1)
    return None


def main(args=None):
    rclpy.init(args=args)
    node = VelocityController()

    # Save terminal settings
    old_settings = termios.tcgetattr(sys.stdin)

    try:
        # Set terminal to raw mode
        tty.setraw(sys.stdin.fileno())

        while rclpy.ok():
            key = get_key()
            if key:
                if key == '\x03':  # Ctrl+C
                    break
                node.process_key(key)

            rclpy.spin_once(node, timeout_sec=0.01)

    except Exception as e:
        print(f'Error: {e}')
    finally:
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
