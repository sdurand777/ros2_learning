// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros2_learning_msg:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__STRUCT_HPP_
#define ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__STRUCT_HPP_

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
// Member 'acceleration'
// Member 'gyroscope'
// Member 'magnetometer'
#include "geometry_msgs/msg/detail/vector3__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros2_learning_msg__msg__SensorData __attribute__((deprecated))
#else
# define DEPRECATED__ros2_learning_msg__msg__SensorData __declspec(deprecated)
#endif

namespace ros2_learning_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SensorData_
{
  using Type = SensorData_<ContainerAllocator>;

  explicit SensorData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    acceleration(_init),
    gyroscope(_init),
    magnetometer(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pressure = 0.0f;
      this->depth = 0.0f;
      this->temperature = 0.0f;
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->altitude = 0.0f;
      this->is_valid = false;
      this->confidence = 0.0f;
    }
  }

  explicit SensorData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    acceleration(_alloc, _init),
    gyroscope(_alloc, _init),
    magnetometer(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pressure = 0.0f;
      this->depth = 0.0f;
      this->temperature = 0.0f;
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->altitude = 0.0f;
      this->is_valid = false;
      this->confidence = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _acceleration_type =
    geometry_msgs::msg::Vector3_<ContainerAllocator>;
  _acceleration_type acceleration;
  using _gyroscope_type =
    geometry_msgs::msg::Vector3_<ContainerAllocator>;
  _gyroscope_type gyroscope;
  using _magnetometer_type =
    geometry_msgs::msg::Vector3_<ContainerAllocator>;
  _magnetometer_type magnetometer;
  using _pressure_type =
    float;
  _pressure_type pressure;
  using _depth_type =
    float;
  _depth_type depth;
  using _temperature_type =
    float;
  _temperature_type temperature;
  using _latitude_type =
    double;
  _latitude_type latitude;
  using _longitude_type =
    double;
  _longitude_type longitude;
  using _altitude_type =
    float;
  _altitude_type altitude;
  using _is_valid_type =
    bool;
  _is_valid_type is_valid;
  using _confidence_type =
    float;
  _confidence_type confidence;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__acceleration(
    const geometry_msgs::msg::Vector3_<ContainerAllocator> & _arg)
  {
    this->acceleration = _arg;
    return *this;
  }
  Type & set__gyroscope(
    const geometry_msgs::msg::Vector3_<ContainerAllocator> & _arg)
  {
    this->gyroscope = _arg;
    return *this;
  }
  Type & set__magnetometer(
    const geometry_msgs::msg::Vector3_<ContainerAllocator> & _arg)
  {
    this->magnetometer = _arg;
    return *this;
  }
  Type & set__pressure(
    const float & _arg)
  {
    this->pressure = _arg;
    return *this;
  }
  Type & set__depth(
    const float & _arg)
  {
    this->depth = _arg;
    return *this;
  }
  Type & set__temperature(
    const float & _arg)
  {
    this->temperature = _arg;
    return *this;
  }
  Type & set__latitude(
    const double & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const double & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__altitude(
    const float & _arg)
  {
    this->altitude = _arg;
    return *this;
  }
  Type & set__is_valid(
    const bool & _arg)
  {
    this->is_valid = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros2_learning_msg::msg::SensorData_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros2_learning_msg::msg::SensorData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::msg::SensorData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros2_learning_msg::msg::SensorData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros2_learning_msg__msg__SensorData
    std::shared_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros2_learning_msg__msg__SensorData
    std::shared_ptr<ros2_learning_msg::msg::SensorData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SensorData_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->acceleration != other.acceleration) {
      return false;
    }
    if (this->gyroscope != other.gyroscope) {
      return false;
    }
    if (this->magnetometer != other.magnetometer) {
      return false;
    }
    if (this->pressure != other.pressure) {
      return false;
    }
    if (this->depth != other.depth) {
      return false;
    }
    if (this->temperature != other.temperature) {
      return false;
    }
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->altitude != other.altitude) {
      return false;
    }
    if (this->is_valid != other.is_valid) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    return true;
  }
  bool operator!=(const SensorData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SensorData_

// alias to use template instance with default allocator
using SensorData =
  ros2_learning_msg::msg::SensorData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__STRUCT_HPP_
