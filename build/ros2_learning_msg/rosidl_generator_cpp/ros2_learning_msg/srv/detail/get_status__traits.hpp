// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ros2_learning_msg:srv/GetStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__TRAITS_HPP_
#define ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ros2_learning_msg/srv/detail/get_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ros2_learning_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetStatus_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_name
  {
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetStatus_Request & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetStatus_Request & msg, bool use_flow_style = false)
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
  const ros2_learning_msg::srv::GetStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_learning_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_learning_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const ros2_learning_msg::srv::GetStatus_Request & msg)
{
  return ros2_learning_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_learning_msg::srv::GetStatus_Request>()
{
  return "ros2_learning_msg::srv::GetStatus_Request";
}

template<>
inline const char * name<ros2_learning_msg::srv::GetStatus_Request>()
{
  return "ros2_learning_msg/srv/GetStatus_Request";
}

template<>
struct has_fixed_size<ros2_learning_msg::srv::GetStatus_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros2_learning_msg::srv::GetStatus_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros2_learning_msg::srv::GetStatus_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'status'
#include "ros2_learning_msg/msg/detail/robot_status__traits.hpp"

namespace ros2_learning_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetStatus_Response & msg,
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

  // member: status
  {
    out << "status: ";
    to_flow_style_yaml(msg.status, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetStatus_Response & msg,
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

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status:\n";
    to_block_style_yaml(msg.status, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetStatus_Response & msg, bool use_flow_style = false)
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
  const ros2_learning_msg::srv::GetStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_learning_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_learning_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const ros2_learning_msg::srv::GetStatus_Response & msg)
{
  return ros2_learning_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_learning_msg::srv::GetStatus_Response>()
{
  return "ros2_learning_msg::srv::GetStatus_Response";
}

template<>
inline const char * name<ros2_learning_msg::srv::GetStatus_Response>()
{
  return "ros2_learning_msg/srv/GetStatus_Response";
}

template<>
struct has_fixed_size<ros2_learning_msg::srv::GetStatus_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros2_learning_msg::srv::GetStatus_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros2_learning_msg::srv::GetStatus_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ros2_learning_msg::srv::GetStatus>()
{
  return "ros2_learning_msg::srv::GetStatus";
}

template<>
inline const char * name<ros2_learning_msg::srv::GetStatus>()
{
  return "ros2_learning_msg/srv/GetStatus";
}

template<>
struct has_fixed_size<ros2_learning_msg::srv::GetStatus>
  : std::integral_constant<
    bool,
    has_fixed_size<ros2_learning_msg::srv::GetStatus_Request>::value &&
    has_fixed_size<ros2_learning_msg::srv::GetStatus_Response>::value
  >
{
};

template<>
struct has_bounded_size<ros2_learning_msg::srv::GetStatus>
  : std::integral_constant<
    bool,
    has_bounded_size<ros2_learning_msg::srv::GetStatus_Request>::value &&
    has_bounded_size<ros2_learning_msg::srv::GetStatus_Response>::value
  >
{
};

template<>
struct is_service<ros2_learning_msg::srv::GetStatus>
  : std::true_type
{
};

template<>
struct is_service_request<ros2_learning_msg::srv::GetStatus_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ros2_learning_msg::srv::GetStatus_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__TRAITS_HPP_
