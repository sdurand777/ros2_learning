// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros2_learning_msg:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_
#define ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros2_learning_msg/msg/detail/sensor_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros2_learning_msg
{

namespace msg
{

namespace builder
{

class Init_SensorData_confidence
{
public:
  explicit Init_SensorData_confidence(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  ::ros2_learning_msg::msg::SensorData confidence(::ros2_learning_msg::msg::SensorData::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_is_valid
{
public:
  explicit Init_SensorData_is_valid(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_confidence is_valid(::ros2_learning_msg::msg::SensorData::_is_valid_type arg)
  {
    msg_.is_valid = std::move(arg);
    return Init_SensorData_confidence(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_altitude
{
public:
  explicit Init_SensorData_altitude(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_is_valid altitude(::ros2_learning_msg::msg::SensorData::_altitude_type arg)
  {
    msg_.altitude = std::move(arg);
    return Init_SensorData_is_valid(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_longitude
{
public:
  explicit Init_SensorData_longitude(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_altitude longitude(::ros2_learning_msg::msg::SensorData::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_SensorData_altitude(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_latitude
{
public:
  explicit Init_SensorData_latitude(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_longitude latitude(::ros2_learning_msg::msg::SensorData::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_SensorData_longitude(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_temperature
{
public:
  explicit Init_SensorData_temperature(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_latitude temperature(::ros2_learning_msg::msg::SensorData::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_SensorData_latitude(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_depth
{
public:
  explicit Init_SensorData_depth(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_temperature depth(::ros2_learning_msg::msg::SensorData::_depth_type arg)
  {
    msg_.depth = std::move(arg);
    return Init_SensorData_temperature(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_pressure
{
public:
  explicit Init_SensorData_pressure(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_depth pressure(::ros2_learning_msg::msg::SensorData::_pressure_type arg)
  {
    msg_.pressure = std::move(arg);
    return Init_SensorData_depth(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_magnetometer
{
public:
  explicit Init_SensorData_magnetometer(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_pressure magnetometer(::ros2_learning_msg::msg::SensorData::_magnetometer_type arg)
  {
    msg_.magnetometer = std::move(arg);
    return Init_SensorData_pressure(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_gyroscope
{
public:
  explicit Init_SensorData_gyroscope(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_magnetometer gyroscope(::ros2_learning_msg::msg::SensorData::_gyroscope_type arg)
  {
    msg_.gyroscope = std::move(arg);
    return Init_SensorData_magnetometer(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_acceleration
{
public:
  explicit Init_SensorData_acceleration(::ros2_learning_msg::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_gyroscope acceleration(::ros2_learning_msg::msg::SensorData::_acceleration_type arg)
  {
    msg_.acceleration = std::move(arg);
    return Init_SensorData_gyroscope(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

class Init_SensorData_header
{
public:
  Init_SensorData_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SensorData_acceleration header(::ros2_learning_msg::msg::SensorData::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_SensorData_acceleration(msg_);
  }

private:
  ::ros2_learning_msg::msg::SensorData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_learning_msg::msg::SensorData>()
{
  return ros2_learning_msg::msg::builder::Init_SensorData_header();
}

}  // namespace ros2_learning_msg

#endif  // ROS2_LEARNING_MSG__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_
