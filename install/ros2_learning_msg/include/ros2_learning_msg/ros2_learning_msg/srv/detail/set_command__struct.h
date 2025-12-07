// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros2_learning_msg:srv/SetCommand.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__STRUCT_H_
#define ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'CMD_ARM'.
/**
  * Command type constants
 */
enum
{
  ros2_learning_msg__srv__SetCommand_Request__CMD_ARM = 0
};

/// Constant 'CMD_DISARM'.
enum
{
  ros2_learning_msg__srv__SetCommand_Request__CMD_DISARM = 1
};

/// Constant 'CMD_SET_MODE'.
enum
{
  ros2_learning_msg__srv__SetCommand_Request__CMD_SET_MODE = 2
};

/// Constant 'CMD_SET_DEPTH'.
enum
{
  ros2_learning_msg__srv__SetCommand_Request__CMD_SET_DEPTH = 3
};

/// Constant 'CMD_SET_HEADING'.
enum
{
  ros2_learning_msg__srv__SetCommand_Request__CMD_SET_HEADING = 4
};

/// Constant 'CMD_MOVE'.
enum
{
  ros2_learning_msg__srv__SetCommand_Request__CMD_MOVE = 5
};

// Include directives for member types
// Member 'robot_name'
#include "rosidl_runtime_c/string.h"
// Member 'parameters'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/SetCommand in the package ros2_learning_msg.
typedef struct ros2_learning_msg__srv__SetCommand_Request
{
  rosidl_runtime_c__String robot_name;
  uint8_t command_type;
  rosidl_runtime_c__float__Sequence parameters;
} ros2_learning_msg__srv__SetCommand_Request;

// Struct for a sequence of ros2_learning_msg__srv__SetCommand_Request.
typedef struct ros2_learning_msg__srv__SetCommand_Request__Sequence
{
  ros2_learning_msg__srv__SetCommand_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_learning_msg__srv__SetCommand_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SetCommand in the package ros2_learning_msg.
typedef struct ros2_learning_msg__srv__SetCommand_Response
{
  bool success;
  rosidl_runtime_c__String message;
  uint32_t command_id;
} ros2_learning_msg__srv__SetCommand_Response;

// Struct for a sequence of ros2_learning_msg__srv__SetCommand_Response.
typedef struct ros2_learning_msg__srv__SetCommand_Response__Sequence
{
  ros2_learning_msg__srv__SetCommand_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_learning_msg__srv__SetCommand_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__STRUCT_H_
