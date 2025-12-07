// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros2_learning_msg:srv/SetCommand.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__BUILDER_HPP_
#define ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros2_learning_msg/srv/detail/set_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros2_learning_msg
{

namespace srv
{

namespace builder
{

class Init_SetCommand_Request_parameters
{
public:
  explicit Init_SetCommand_Request_parameters(::ros2_learning_msg::srv::SetCommand_Request & msg)
  : msg_(msg)
  {}
  ::ros2_learning_msg::srv::SetCommand_Request parameters(::ros2_learning_msg::srv::SetCommand_Request::_parameters_type arg)
  {
    msg_.parameters = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_learning_msg::srv::SetCommand_Request msg_;
};

class Init_SetCommand_Request_command_type
{
public:
  explicit Init_SetCommand_Request_command_type(::ros2_learning_msg::srv::SetCommand_Request & msg)
  : msg_(msg)
  {}
  Init_SetCommand_Request_parameters command_type(::ros2_learning_msg::srv::SetCommand_Request::_command_type_type arg)
  {
    msg_.command_type = std::move(arg);
    return Init_SetCommand_Request_parameters(msg_);
  }

private:
  ::ros2_learning_msg::srv::SetCommand_Request msg_;
};

class Init_SetCommand_Request_robot_name
{
public:
  Init_SetCommand_Request_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetCommand_Request_command_type robot_name(::ros2_learning_msg::srv::SetCommand_Request::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return Init_SetCommand_Request_command_type(msg_);
  }

private:
  ::ros2_learning_msg::srv::SetCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_learning_msg::srv::SetCommand_Request>()
{
  return ros2_learning_msg::srv::builder::Init_SetCommand_Request_robot_name();
}

}  // namespace ros2_learning_msg


namespace ros2_learning_msg
{

namespace srv
{

namespace builder
{

class Init_SetCommand_Response_command_id
{
public:
  explicit Init_SetCommand_Response_command_id(::ros2_learning_msg::srv::SetCommand_Response & msg)
  : msg_(msg)
  {}
  ::ros2_learning_msg::srv::SetCommand_Response command_id(::ros2_learning_msg::srv::SetCommand_Response::_command_id_type arg)
  {
    msg_.command_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_learning_msg::srv::SetCommand_Response msg_;
};

class Init_SetCommand_Response_message
{
public:
  explicit Init_SetCommand_Response_message(::ros2_learning_msg::srv::SetCommand_Response & msg)
  : msg_(msg)
  {}
  Init_SetCommand_Response_command_id message(::ros2_learning_msg::srv::SetCommand_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return Init_SetCommand_Response_command_id(msg_);
  }

private:
  ::ros2_learning_msg::srv::SetCommand_Response msg_;
};

class Init_SetCommand_Response_success
{
public:
  Init_SetCommand_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetCommand_Response_message success(::ros2_learning_msg::srv::SetCommand_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SetCommand_Response_message(msg_);
  }

private:
  ::ros2_learning_msg::srv::SetCommand_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_learning_msg::srv::SetCommand_Response>()
{
  return ros2_learning_msg::srv::builder::Init_SetCommand_Response_success();
}

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__SET_COMMAND__BUILDER_HPP_
