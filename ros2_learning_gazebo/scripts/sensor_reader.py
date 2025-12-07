#!/usr/bin/env python3
"""
Sensor Reader Node.
Subscribes to various sensor topics from Gazebo and processes them.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, Image, CameraInfo, LaserScan, PointCloud2
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64
import math


class SensorReader(Node):
    def __init__(self):
        super().__init__('sensor_reader')

        # Declare parameters
        self.declare_parameter('robot_name', 'bluerov2')
        self.declare_parameter('log_rate', 1.0)  # Hz

        self.robot_name = self.get_parameter('robot_name').value
        self.log_rate = self.get_parameter('log_rate').value

        # Sensor data storage
        self.imu_data = None
        self.depth_data = None
        self.camera_data = None
        self.lidar_data = None

        # Subscribers
        self.imu_sub = self.create_subscription(
            Imu, 'imu/data', self.imu_callback, 10
        )

        self.depth_sub = self.create_subscription(
            Float64, 'depth', self.depth_callback, 10
        )

        self.camera_sub = self.create_subscription(
            Image, 'camera/image_raw', self.camera_callback, 10
        )

        self.camera_info_sub = self.create_subscription(
            CameraInfo, 'camera/camera_info', self.camera_info_callback, 10
        )

        self.lidar_sub = self.create_subscription(
            LaserScan, 'scan', self.lidar_callback, 10
        )

        # Timer for logging
        if self.log_rate > 0:
            self.log_timer = self.create_timer(1.0 / self.log_rate, self.log_sensor_data)

        self.get_logger().info(f'Sensor Reader initialized for {self.robot_name}')

    def imu_callback(self, msg: Imu):
        """Process IMU data."""
        self.imu_data = {
            'orientation': msg.orientation,
            'angular_velocity': msg.angular_velocity,
            'linear_acceleration': msg.linear_acceleration,
            'timestamp': msg.header.stamp
        }

    def depth_callback(self, msg: Float64):
        """Process depth sensor data."""
        self.depth_data = msg.data

    def camera_callback(self, msg: Image):
        """Process camera image."""
        self.camera_data = {
            'width': msg.width,
            'height': msg.height,
            'encoding': msg.encoding,
            'timestamp': msg.header.stamp
        }

    def camera_info_callback(self, msg: CameraInfo):
        """Process camera info."""
        pass  # Can extract intrinsics here if needed

    def lidar_callback(self, msg: LaserScan):
        """Process LiDAR data."""
        # Find minimum distance (closest obstacle)
        valid_ranges = [r for r in msg.ranges if msg.range_min < r < msg.range_max]

        self.lidar_data = {
            'range_min': msg.range_min,
            'range_max': msg.range_max,
            'angle_min': msg.angle_min,
            'angle_max': msg.angle_max,
            'num_readings': len(msg.ranges),
            'min_distance': min(valid_ranges) if valid_ranges else float('inf'),
            'timestamp': msg.header.stamp
        }

    def log_sensor_data(self):
        """Log current sensor status."""
        lines = ['\n=== Sensor Status ===']

        if self.imu_data:
            acc = self.imu_data['linear_acceleration']
            gyro = self.imu_data['angular_velocity']
            lines.append(
                f'IMU: acc=({acc.x:.2f}, {acc.y:.2f}, {acc.z:.2f}) '
                f'gyro=({gyro.x:.3f}, {gyro.y:.3f}, {gyro.z:.3f})'
            )

            # Calculate roll/pitch from accelerometer
            roll = math.atan2(acc.y, acc.z) * 180 / math.pi
            pitch = math.atan2(-acc.x, math.sqrt(acc.y**2 + acc.z**2)) * 180 / math.pi
            lines.append(f'     roll={roll:.1f}° pitch={pitch:.1f}°')
        else:
            lines.append('IMU: No data')

        if self.depth_data is not None:
            lines.append(f'Depth: {self.depth_data:.2f} m')
        else:
            lines.append('Depth: No data')

        if self.camera_data:
            lines.append(
                f'Camera: {self.camera_data["width"]}x{self.camera_data["height"]} '
                f'({self.camera_data["encoding"]})'
            )
        else:
            lines.append('Camera: No data')

        if self.lidar_data:
            lines.append(
                f'LiDAR: {self.lidar_data["num_readings"]} readings, '
                f'closest={self.lidar_data["min_distance"]:.2f}m'
            )
        else:
            lines.append('LiDAR: No data')

        lines.append('=' * 20)
        self.get_logger().info('\n'.join(lines))

    def get_imu_euler(self) -> tuple:
        """Get Euler angles from IMU quaternion."""
        if not self.imu_data:
            return None

        q = self.imu_data['orientation']

        # Roll
        sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
        cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
        roll = math.atan2(sinr_cosp, cosr_cosp)

        # Pitch
        sinp = 2 * (q.w * q.y - q.z * q.x)
        pitch = math.asin(max(-1, min(1, sinp)))

        # Yaw
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw


def main(args=None):
    rclpy.init(args=args)
    node = SensorReader()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
