// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros2_learning_msg:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_
#define ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'MODE_MANUAL'.
/**
  * Mode constants
 */
enum
{
  ros2_learning_msg__msg__RobotStatus__MODE_MANUAL = 0
};

/// Constant 'MODE_STABILIZE'.
enum
{
  ros2_learning_msg__msg__RobotStatus__MODE_STABILIZE = 1
};

/// Constant 'MODE_DEPTH_HOLD'.
enum
{
  ros2_learning_msg__msg__RobotStatus__MODE_DEPTH_HOLD = 2
};

/// Constant 'MODE_AUTO'.
enum
{
  ros2_learning_msg__msg__RobotStatus__MODE_AUTO = 3
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'robot_name'
#include "rosidl_runtime_c/string.h"
// Member 'position'
#include "geometry_msgs/msg/detail/point__struct.h"
// Member 'orientation'
#include "geometry_msgs/msg/detail/quaternion__struct.h"
// Member 'velocity'
#include "geometry_msgs/msg/detail/twist__struct.h"

/// Struct defined in msg/RobotStatus in the package ros2_learning_msg.
/**
  * Custom message for robot status
 */
typedef struct ros2_learning_msg__msg__RobotStatus
{
  std_msgs__msg__Header header;
  /// Robot identification
  rosidl_runtime_c__String robot_name;
  uint32_t robot_id;
  /// Position (x, y, z)
  geometry_msgs__msg__Point position;
  /// Orientation (quaternion)
  geometry_msgs__msg__Quaternion orientation;
  /// Velocity (linear and angular)
  geometry_msgs__msg__Twist velocity;
  /// Battery level (0-100%)
  float battery_level;
  /// Status flags
  bool is_armed;
  bool is_connected;
  uint8_t mode;
} ros2_learning_msg__msg__RobotStatus;

// Struct for a sequence of ros2_learning_msg__msg__RobotStatus.
typedef struct ros2_learning_msg__msg__RobotStatus__Sequence
{
  ros2_learning_msg__msg__RobotStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_learning_msg__msg__RobotStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_
