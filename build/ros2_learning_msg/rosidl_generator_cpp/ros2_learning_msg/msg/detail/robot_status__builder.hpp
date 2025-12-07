// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros2_learning_msg:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_
#define ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros2_learning_msg/msg/detail/robot_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros2_learning_msg
{

namespace msg
{

namespace builder
{

class Init_RobotStatus_mode
{
public:
  explicit Init_RobotStatus_mode(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  ::ros2_learning_msg::msg::RobotStatus mode(::ros2_learning_msg::msg::RobotStatus::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_is_connected
{
public:
  explicit Init_RobotStatus_is_connected(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_mode is_connected(::ros2_learning_msg::msg::RobotStatus::_is_connected_type arg)
  {
    msg_.is_connected = std::move(arg);
    return Init_RobotStatus_mode(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_is_armed
{
public:
  explicit Init_RobotStatus_is_armed(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_is_connected is_armed(::ros2_learning_msg::msg::RobotStatus::_is_armed_type arg)
  {
    msg_.is_armed = std::move(arg);
    return Init_RobotStatus_is_connected(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_battery_level
{
public:
  explicit Init_RobotStatus_battery_level(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_is_armed battery_level(::ros2_learning_msg::msg::RobotStatus::_battery_level_type arg)
  {
    msg_.battery_level = std::move(arg);
    return Init_RobotStatus_is_armed(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_velocity
{
public:
  explicit Init_RobotStatus_velocity(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_battery_level velocity(::ros2_learning_msg::msg::RobotStatus::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_RobotStatus_battery_level(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_orientation
{
public:
  explicit Init_RobotStatus_orientation(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_velocity orientation(::ros2_learning_msg::msg::RobotStatus::_orientation_type arg)
  {
    msg_.orientation = std::move(arg);
    return Init_RobotStatus_velocity(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_position
{
public:
  explicit Init_RobotStatus_position(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_orientation position(::ros2_learning_msg::msg::RobotStatus::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_RobotStatus_orientation(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_robot_id
{
public:
  explicit Init_RobotStatus_robot_id(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_position robot_id(::ros2_learning_msg::msg::RobotStatus::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_RobotStatus_position(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_robot_name
{
public:
  explicit Init_RobotStatus_robot_name(::ros2_learning_msg::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_robot_id robot_name(::ros2_learning_msg::msg::RobotStatus::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return Init_RobotStatus_robot_id(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

class Init_RobotStatus_header
{
public:
  Init_RobotStatus_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotStatus_robot_name header(::ros2_learning_msg::msg::RobotStatus::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RobotStatus_robot_name(msg_);
  }

private:
  ::ros2_learning_msg::msg::RobotStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_learning_msg::msg::RobotStatus>()
{
  return ros2_learning_msg::msg::builder::Init_RobotStatus_header();
}

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_
