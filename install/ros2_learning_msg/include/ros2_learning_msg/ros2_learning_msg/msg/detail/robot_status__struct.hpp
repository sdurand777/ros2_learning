// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros2_learning_msg:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__STRUCT_HPP_
#define ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'position'
#include "geometry_msgs/msg/detail/point__struct.hpp"
// Member 'orientation'
#include "geometry_msgs/msg/detail/quaternion__struct.hpp"
// Member 'velocity'
#include "geometry_msgs/msg/detail/twist__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros2_learning_msg__msg__RobotStatus __attribute__((deprecated))
#else
# define DEPRECATED__ros2_learning_msg__msg__RobotStatus __declspec(deprecated)
#endif

namespace ros2_learning_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotStatus_
{
  using Type = RobotStatus_<ContainerAllocator>;

  explicit RobotStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    position(_init),
    orientation(_init),
    velocity(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->robot_id = 0ul;
      this->battery_level = 0.0f;
      this->is_armed = false;
      this->is_connected = false;
      this->mode = 0;
    }
  }

  explicit RobotStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    robot_name(_alloc),
    position(_alloc, _init),
    orientation(_alloc, _init),
    velocity(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->robot_id = 0ul;
      this->battery_level = 0.0f;
      this->is_armed = false;
      this->is_connected = false;
      this->mode = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _robot_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _robot_name_type robot_name;
  using _robot_id_type =
    uint32_t;
  _robot_id_type robot_id;
  using _position_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _position_type position;
  using _orientation_type =
    geometry_msgs::msg::Quaternion_<ContainerAllocator>;
  _orientation_type orientation;
  using _velocity_type =
    geometry_msgs::msg::Twist_<ContainerAllocator>;
  _velocity_type velocity;
  using _battery_level_type =
    float;
  _battery_level_type battery_level;
  using _is_armed_type =
    bool;
  _is_armed_type is_armed;
  using _is_connected_type =
    bool;
  _is_connected_type is_connected;
  using _mode_type =
    uint8_t;
  _mode_type mode;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__robot_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->robot_name = _arg;
    return *this;
  }
  Type & set__robot_id(
    const uint32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__position(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->position = _arg;
    return *this;
  }
  Type & set__orientation(
    const geometry_msgs::msg::Quaternion_<ContainerAllocator> & _arg)
  {
    this->orientation = _arg;
    return *this;
  }
  Type & set__velocity(
    const geometry_msgs::msg::Twist_<ContainerAllocator> & _arg)
  {
    this->velocity = _arg;
    return *this;
  }
  Type & set__battery_level(
    const float & _arg)
  {
    this->battery_level = _arg;
    return *this;
  }
  Type & set__is_armed(
    const bool & _arg)
  {
    this->is_armed = _arg;
    return *this;
  }
  Type & set__is_connected(
    const bool & _arg)
  {
    this->is_connected = _arg;
    return *this;
  }
  Type & set__mode(
    const uint8_t & _arg)
  {
    this->mode = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t MODE_MANUAL =
    0u;
  static constexpr uint8_t MODE_STABILIZE =
    1u;
  static constexpr uint8_t MODE_DEPTH_HOLD =
    2u;
  static constexpr uint8_t MODE_AUTO =
    3u;

  // pointer types
  using RawPtr =
    ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros2_learning_msg__msg__RobotStatus
    std::shared_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros2_learning_msg__msg__RobotStatus
    std::shared_ptr<ros2_learning_msg::msg::RobotStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotStatus_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->robot_name != other.robot_name) {
      return false;
    }
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->position != other.position) {
      return false;
    }
    if (this->orientation != other.orientation) {
      return false;
    }
    if (this->velocity != other.velocity) {
      return false;
    }
    if (this->battery_level != other.battery_level) {
      return false;
    }
    if (this->is_armed != other.is_armed) {
      return false;
    }
    if (this->is_connected != other.is_connected) {
      return false;
    }
    if (this->mode != other.mode) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotStatus_

// alias to use template instance with default allocator
using RobotStatus =
  ros2_learning_msg::msg::RobotStatus_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotStatus_<ContainerAllocator>::MODE_MANUAL;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotStatus_<ContainerAllocator>::MODE_STABILIZE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotStatus_<ContainerAllocator>::MODE_DEPTH_HOLD;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotStatus_<ContainerAllocator>::MODE_AUTO;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__ROBOT_STATUS__STRUCT_HPP_
