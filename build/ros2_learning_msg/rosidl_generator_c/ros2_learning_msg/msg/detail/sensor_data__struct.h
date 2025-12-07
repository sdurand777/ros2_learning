// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros2_learning_msg:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__STRUCT_H_
#define ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'acceleration'
// Member 'gyroscope'
// Member 'magnetometer'
#include "geometry_msgs/msg/detail/vector3__struct.h"

/// Struct defined in msg/SensorData in the package ros2_learning_msg.
/**
  * Custom message for sensor data
 */
typedef struct ros2_learning_msg__msg__SensorData
{
  std_msgs__msg__Header header;
  /// IMU data
  geometry_msgs__msg__Vector3 acceleration;
  geometry_msgs__msg__Vector3 gyroscope;
  geometry_msgs__msg__Vector3 magnetometer;
  /// Pressure/Depth sensor
  /// in Pascals
  float pressure;
  /// in meters
  float depth;
  /// in Celsius
  float temperature;
  /// GPS (if available at surface)
  double latitude;
  double longitude;
  float altitude;
  /// Data quality
  bool is_valid;
  /// 0.0 to 1.0
  float confidence;
} ros2_learning_msg__msg__SensorData;

// Struct for a sequence of ros2_learning_msg__msg__SensorData.
typedef struct ros2_learning_msg__msg__SensorData__Sequence
{
  ros2_learning_msg__msg__SensorData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_learning_msg__msg__SensorData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__STRUCT_H_
