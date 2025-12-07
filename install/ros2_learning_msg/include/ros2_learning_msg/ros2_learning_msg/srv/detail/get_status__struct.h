// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros2_learning_msg:srv/GetStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__STRUCT_H_
#define ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'robot_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetStatus in the package ros2_learning_msg.
typedef struct ros2_learning_msg__srv__GetStatus_Request
{
  rosidl_runtime_c__String robot_name;
} ros2_learning_msg__srv__GetStatus_Request;

// Struct for a sequence of ros2_learning_msg__srv__GetStatus_Request.
typedef struct ros2_learning_msg__srv__GetStatus_Request__Sequence
{
  ros2_learning_msg__srv__GetStatus_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_learning_msg__srv__GetStatus_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"
// Member 'status'
#include "ros2_learning_msg/msg/detail/robot_status__struct.h"

/// Struct defined in srv/GetStatus in the package ros2_learning_msg.
typedef struct ros2_learning_msg__srv__GetStatus_Response
{
  bool success;
  rosidl_runtime_c__String message;
  ros2_learning_msg__msg__RobotStatus status;
} ros2_learning_msg__srv__GetStatus_Response;

// Struct for a sequence of ros2_learning_msg__srv__GetStatus_Response.
typedef struct ros2_learning_msg__srv__GetStatus_Response__Sequence
{
  ros2_learning_msg__srv__GetStatus_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_learning_msg__srv__GetStatus_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__STRUCT_H_
