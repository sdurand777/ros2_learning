// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros2_learning_msg:srv/GetStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__STRUCT_HPP_
#define ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ros2_learning_msg__srv__GetStatus_Request __attribute__((deprecated))
#else
# define DEPRECATED__ros2_learning_msg__srv__GetStatus_Request __declspec(deprecated)
#endif

namespace ros2_learning_msg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetStatus_Request_
{
  using Type = GetStatus_Request_<ContainerAllocator>;

  explicit GetStatus_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
    }
  }

  explicit GetStatus_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
    }
  }

  // field types and members
  using _robot_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _robot_name_type robot_name;

  // setters for named parameter idiom
  Type & set__robot_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->robot_name = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros2_learning_msg__srv__GetStatus_Request
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros2_learning_msg__srv__GetStatus_Request
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetStatus_Request_ & other) const
  {
    if (this->robot_name != other.robot_name) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetStatus_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetStatus_Request_

// alias to use template instance with default allocator
using GetStatus_Request =
  ros2_learning_msg::srv::GetStatus_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros2_learning_msg


// Include directives for member types
// Member 'status'
#include "ros2_learning_msg/msg/detail/robot_status__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros2_learning_msg__srv__GetStatus_Response __attribute__((deprecated))
#else
# define DEPRECATED__ros2_learning_msg__srv__GetStatus_Response __declspec(deprecated)
#endif

namespace ros2_learning_msg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetStatus_Response_
{
  using Type = GetStatus_Response_<ContainerAllocator>;

  explicit GetStatus_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : status(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit GetStatus_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc),
    status(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;
  using _status_type =
    ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>;
  _status_type status;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }
  Type & set__status(
    const ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros2_learning_msg__srv__GetStatus_Response
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros2_learning_msg__srv__GetStatus_Response
    std::shared_ptr<ros2_learning_msg::srv::GetStatus_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetStatus_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetStatus_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetStatus_Response_

// alias to use template instance with default allocator
using GetStatus_Response =
  ros2_learning_msg::srv::GetStatus_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros2_learning_msg

namespace ros2_learning_msg
{

namespace srv
{

struct GetStatus
{
  using Request = ros2_learning_msg::srv::GetStatus_Request;
  using Response = ros2_learning_msg::srv::GetStatus_Response;
};

}  // namespace srv

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__SRV__DETAIL__GET_STATUS__STRUCT_HPP_
