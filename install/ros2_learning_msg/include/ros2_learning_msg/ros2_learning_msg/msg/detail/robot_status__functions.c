// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ros2_learning_msg:msg/RobotStatus.idl
// generated code does not contain a copyright notice
#include "ros2_learning_msg/msg/detail/robot_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `robot_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `position`
#include "geometry_msgs/msg/detail/point__functions.h"
// Member `orientation`
#include "geometry_msgs/msg/detail/quaternion__functions.h"
// Member `velocity`
#include "geometry_msgs/msg/detail/twist__functions.h"

bool
ros2_learning_msg__msg__RobotStatus__init(ros2_learning_msg__msg__RobotStatus * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    ros2_learning_msg__msg__RobotStatus__fini(msg);
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__init(&msg->robot_name)) {
    ros2_learning_msg__msg__RobotStatus__fini(msg);
    return false;
  }
  // robot_id
  // position
  if (!geometry_msgs__msg__Point__init(&msg->position)) {
    ros2_learning_msg__msg__RobotStatus__fini(msg);
    return false;
  }
  // orientation
  if (!geometry_msgs__msg__Quaternion__init(&msg->orientation)) {
    ros2_learning_msg__msg__RobotStatus__fini(msg);
    return false;
  }
  // velocity
  if (!geometry_msgs__msg__Twist__init(&msg->velocity)) {
    ros2_learning_msg__msg__RobotStatus__fini(msg);
    return false;
  }
  // battery_level
  // is_armed
  // is_connected
  // mode
  return true;
}

void
ros2_learning_msg__msg__RobotStatus__fini(ros2_learning_msg__msg__RobotStatus * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // robot_name
  rosidl_runtime_c__String__fini(&msg->robot_name);
  // robot_id
  // position
  geometry_msgs__msg__Point__fini(&msg->position);
  // orientation
  geometry_msgs__msg__Quaternion__fini(&msg->orientation);
  // velocity
  geometry_msgs__msg__Twist__fini(&msg->velocity);
  // battery_level
  // is_armed
  // is_connected
  // mode
}

bool
ros2_learning_msg__msg__RobotStatus__are_equal(const ros2_learning_msg__msg__RobotStatus * lhs, const ros2_learning_msg__msg__RobotStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->robot_name), &(rhs->robot_name)))
  {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // position
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->position), &(rhs->position)))
  {
    return false;
  }
  // orientation
  if (!geometry_msgs__msg__Quaternion__are_equal(
      &(lhs->orientation), &(rhs->orientation)))
  {
    return false;
  }
  // velocity
  if (!geometry_msgs__msg__Twist__are_equal(
      &(lhs->velocity), &(rhs->velocity)))
  {
    return false;
  }
  // battery_level
  if (lhs->battery_level != rhs->battery_level) {
    return false;
  }
  // is_armed
  if (lhs->is_armed != rhs->is_armed) {
    return false;
  }
  // is_connected
  if (lhs->is_connected != rhs->is_connected) {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  return true;
}

bool
ros2_learning_msg__msg__RobotStatus__copy(
  const ros2_learning_msg__msg__RobotStatus * input,
  ros2_learning_msg__msg__RobotStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__copy(
      &(input->robot_name), &(output->robot_name)))
  {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // position
  if (!geometry_msgs__msg__Point__copy(
      &(input->position), &(output->position)))
  {
    return false;
  }
  // orientation
  if (!geometry_msgs__msg__Quaternion__copy(
      &(input->orientation), &(output->orientation)))
  {
    return false;
  }
  // velocity
  if (!geometry_msgs__msg__Twist__copy(
      &(input->velocity), &(output->velocity)))
  {
    return false;
  }
  // battery_level
  output->battery_level = input->battery_level;
  // is_armed
  output->is_armed = input->is_armed;
  // is_connected
  output->is_connected = input->is_connected;
  // mode
  output->mode = input->mode;
  return true;
}

ros2_learning_msg__msg__RobotStatus *
ros2_learning_msg__msg__RobotStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros2_learning_msg__msg__RobotStatus * msg = (ros2_learning_msg__msg__RobotStatus *)allocator.allocate(sizeof(ros2_learning_msg__msg__RobotStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ros2_learning_msg__msg__RobotStatus));
  bool success = ros2_learning_msg__msg__RobotStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ros2_learning_msg__msg__RobotStatus__destroy(ros2_learning_msg__msg__RobotStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ros2_learning_msg__msg__RobotStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ros2_learning_msg__msg__RobotStatus__Sequence__init(ros2_learning_msg__msg__RobotStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros2_learning_msg__msg__RobotStatus * data = NULL;

  if (size) {
    data = (ros2_learning_msg__msg__RobotStatus *)allocator.zero_allocate(size, sizeof(ros2_learning_msg__msg__RobotStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ros2_learning_msg__msg__RobotStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ros2_learning_msg__msg__RobotStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ros2_learning_msg__msg__RobotStatus__Sequence__fini(ros2_learning_msg__msg__RobotStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ros2_learning_msg__msg__RobotStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ros2_learning_msg__msg__RobotStatus__Sequence *
ros2_learning_msg__msg__RobotStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros2_learning_msg__msg__RobotStatus__Sequence * array = (ros2_learning_msg__msg__RobotStatus__Sequence *)allocator.allocate(sizeof(ros2_learning_msg__msg__RobotStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ros2_learning_msg__msg__RobotStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ros2_learning_msg__msg__RobotStatus__Sequence__destroy(ros2_learning_msg__msg__RobotStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ros2_learning_msg__msg__RobotStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ros2_learning_msg__msg__RobotStatus__Sequence__are_equal(const ros2_learning_msg__msg__RobotStatus__Sequence * lhs, const ros2_learning_msg__msg__RobotStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ros2_learning_msg__msg__RobotStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ros2_learning_msg__msg__RobotStatus__Sequence__copy(
  const ros2_learning_msg__msg__RobotStatus__Sequence * input,
  ros2_learning_msg__msg__RobotStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ros2_learning_msg__msg__RobotStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ros2_learning_msg__msg__RobotStatus * data =
      (ros2_learning_msg__msg__RobotStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ros2_learning_msg__msg__RobotStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ros2_learning_msg__msg__RobotStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ros2_learning_msg__msg__RobotStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
