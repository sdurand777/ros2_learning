// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros2_learning_msg:srv/GetStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__BUILDER_HPP_
#define ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros2_learning_msg/srv/detail/get_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros2_learning_msg
{

namespace srv
{

namespace builder
{

class Init_GetStatus_Request_robot_name
{
public:
  Init_GetStatus_Request_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ros2_learning_msg::srv::GetStatus_Request robot_name(::ros2_learning_msg::srv::GetStatus_Request::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_learning_msg::srv::GetStatus_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_learning_msg::srv::GetStatus_Request>()
{
  return ros2_learning_msg::srv::builder::Init_GetStatus_Request_robot_name();
}

}  // namespace ros2_learning_msg


namespace ros2_learning_msg
{

namespace srv
{

namespace builder
{

class Init_GetStatus_Response_status
{
public:
  explicit Init_GetStatus_Response_status(::ros2_learning_msg::srv::GetStatus_Response & msg)
  : msg_(msg)
  {}
  ::ros2_learning_msg::srv::GetStatus_Response status(::ros2_learning_msg::srv::GetStatus_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_learning_msg::srv::GetStatus_Response msg_;
};

class Init_GetStatus_Response_message
{
public:
  explicit Init_GetStatus_Response_message(::ros2_learning_msg::srv::GetStatus_Response & msg)
  : msg_(msg)
  {}
  Init_GetStatus_Response_status message(::ros2_learning_msg::srv::GetStatus_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return Init_GetStatus_Response_status(msg_);
  }

private:
  ::ros2_learning_msg::srv::GetStatus_Response msg_;
};

class Init_GetStatus_Response_success
{
public:
  Init_GetStatus_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetStatus_Response_message success(::ros2_learning_msg::srv::GetStatus_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_GetStatus_Response_message(msg_);
  }

private:
  ::ros2_learning_msg::srv::GetStatus_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_learning_msg::srv::GetStatus_Response>()
{
  return ros2_learning_msg::srv::builder::Init_GetStatus_Response_success();
}

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__BUILDER_HPP_
