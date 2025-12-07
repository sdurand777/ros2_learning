// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ros2_learning_msg:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__TRAITS_HPP_
#define ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ros2_learning_msg/msg/detail/sensor_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'acceleration'
// Member 'gyroscope'
// Member 'magnetometer'
#include "geometry_msgs/msg/detail/vector3__traits.hpp"

namespace ros2_learning_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const SensorData & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: acceleration
  {
    out << "acceleration: ";
    to_flow_style_yaml(msg.acceleration, out);
    out << ", ";
  }

  // member: gyroscope
  {
    out << "gyroscope: ";
    to_flow_style_yaml(msg.gyroscope, out);
    out << ", ";
  }

  // member: magnetometer
  {
    out << "magnetometer: ";
    to_flow_style_yaml(msg.magnetometer, out);
    out << ", ";
  }

  // member: pressure
  {
    out << "pressure: ";
    rosidl_generator_traits::value_to_yaml(msg.pressure, out);
    out << ", ";
  }

  // member: depth
  {
    out << "depth: ";
    rosidl_generator_traits::value_to_yaml(msg.depth, out);
    out << ", ";
  }

  // member: temperature
  {
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << ", ";
  }

  // member: latitude
  {
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << ", ";
  }

  // member: longitude
  {
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << ", ";
  }

  // member: altitude
  {
    out << "altitude: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude, out);
    out << ", ";
  }

  // member: is_valid
  {
    out << "is_valid: ";
    rosidl_generator_traits::value_to_yaml(msg.is_valid, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SensorData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: acceleration
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acceleration:\n";
    to_block_style_yaml(msg.acceleration, out, indentation + 2);
  }

  // member: gyroscope
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyroscope:\n";
    to_block_style_yaml(msg.gyroscope, out, indentation + 2);
  }

  // member: magnetometer
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "magnetometer:\n";
    to_block_style_yaml(msg.magnetometer, out, indentation + 2);
  }

  // member: pressure
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pressure: ";
    rosidl_generator_traits::value_to_yaml(msg.pressure, out);
    out << "\n";
  }

  // member: depth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "depth: ";
    rosidl_generator_traits::value_to_yaml(msg.depth, out);
    out << "\n";
  }

  // member: temperature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << "\n";
  }

  // member: latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << "\n";
  }

  // member: longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << "\n";
  }

  // member: altitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "altitude: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude, out);
    out << "\n";
  }

  // member: is_valid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_valid: ";
    rosidl_generator_traits::value_to_yaml(msg.is_valid, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SensorData & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ros2_learning_msg

namespace rosidl_generator_traits
{

[[deprecated("use ros2_learning_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros2_learning_msg::msg::SensorData & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_learning_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_learning_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const ros2_learning_msg::msg::SensorData & msg)
{
  return ros2_learning_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_learning_msg::msg::SensorData>()
{
  return "ros2_learning_msg::msg::SensorData";
}

template<>
inline const char * name<ros2_learning_msg::msg::SensorData>()
{
  return "ros2_learning_msg/msg/SensorData";
}

template<>
struct has_fixed_size<ros2_learning_msg::msg::SensorData>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Vector3>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<ros2_learning_msg::msg::SensorData>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Vector3>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<ros2_learning_msg::msg::SensorData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__TRAITS_HPP_
