// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ros2_learning_msg:srv/SetCommand.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__TRAITS_HPP_
#define ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ros2_learning_msg/srv/detail/set_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ros2_learning_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetCommand_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_name
  {
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
    out << ", ";
  }

  // member: command_type
  {
    out << "command_type: ";
    rosidl_generator_traits::value_to_yaml(msg.command_type, out);
    out << ", ";
  }

  // member: parameters
  {
    if (msg.parameters.size() == 0) {
      out << "parameters: []";
    } else {
      out << "parameters: [";
      size_t pending_items = msg.parameters.size();
      for (auto item : msg.parameters) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
    out << "\n";
  }

  // member: command_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command_type: ";
    rosidl_generator_traits::value_to_yaml(msg.command_type, out);
    out << "\n";
  }

  // member: parameters
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.parameters.size() == 0) {
      out << "parameters: []\n";
    } else {
      out << "parameters:\n";
      for (auto item : msg.parameters) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetCommand_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ros2_learning_msg

namespace rosidl_generator_traits
{

[[deprecated("use ros2_learning_msg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros2_learning_msg::srv::SetCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_learning_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_learning_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const ros2_learning_msg::srv::SetCommand_Request & msg)
{
  return ros2_learning_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_learning_msg::srv::SetCommand_Request>()
{
  return "ros2_learning_msg::srv::SetCommand_Request";
}

template<>
inline const char * name<ros2_learning_msg::srv::SetCommand_Request>()
{
  return "ros2_learning_msg/srv/SetCommand_Request";
}

template<>
struct has_fixed_size<ros2_learning_msg::srv::SetCommand_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros2_learning_msg::srv::SetCommand_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros2_learning_msg::srv::SetCommand_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace ros2_learning_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetCommand_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << ", ";
  }

  // member: command_id
  {
    out << "command_id: ";
    rosidl_generator_traits::value_to_yaml(msg.command_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }

  // member: command_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command_id: ";
    rosidl_generator_traits::value_to_yaml(msg.command_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetCommand_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ros2_learning_msg

namespace rosidl_generator_traits
{

[[deprecated("use ros2_learning_msg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros2_learning_msg::srv::SetCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_learning_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_learning_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const ros2_learning_msg::srv::SetCommand_Response & msg)
{
  return ros2_learning_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_learning_msg::srv::SetCommand_Response>()
{
  return "ros2_learning_msg::srv::SetCommand_Response";
}

template<>
inline const char * name<ros2_learning_msg::srv::SetCommand_Response>()
{
  return "ros2_learning_msg/srv/SetCommand_Response";
}

template<>
struct has_fixed_size<ros2_learning_msg::srv::SetCommand_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros2_learning_msg::srv::SetCommand_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros2_learning_msg::srv::SetCommand_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ros2_learning_msg::srv::SetCommand>()
{
  return "ros2_learning_msg::srv::SetCommand";
}

template<>
inline const char * name<ros2_learning_msg::srv::SetCommand>()
{
  return "ros2_learning_msg/srv/SetCommand";
}

template<>
struct has_fixed_size<ros2_learning_msg::srv::SetCommand>
  : std::integral_constant<
    bool,
    has_fixed_size<ros2_learning_msg::srv::SetCommand_Request>::value &&
    has_fixed_size<ros2_learning_msg::srv::SetCommand_Response>::value
  >
{
};

template<>
struct has_bounded_size<ros2_learning_msg::srv::SetCommand>
  : std::integral_constant<
    bool,
    has_bounded_size<ros2_learning_msg::srv::SetCommand_Request>::value &&
    has_bounded_size<ros2_learning_msg::srv::SetCommand_Response>::value
  >
{
};

template<>
struct is_service<ros2_learning_msg::srv::SetCommand>
  : std::true_type
{
};

template<>
struct is_service_request<ros2_learning_msg::srv::SetCommand_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ros2_learning_msg::srv::SetCommand_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__TRAITS_HPP_
