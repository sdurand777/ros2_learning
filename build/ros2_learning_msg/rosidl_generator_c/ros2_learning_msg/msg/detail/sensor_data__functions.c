// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ros2_learning_msg:msg/SensorData.idl
// generated code does not contain a copyright notice
#include "ros2_learning_msg/msg/detail/sensor_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `acceleration`
// Member `gyroscope`
// Member `magnetometer`
#include "geometry_msgs/msg/detail/vector3__functions.h"

bool
ros2_learning_msg__msg__SensorData__init(ros2_learning_msg__msg__SensorData * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    ros2_learning_msg__msg__SensorData__fini(msg);
    return false;
  }
  // acceleration
  if (!geometry_msgs__msg__Vector3__init(&msg->acceleration)) {
    ros2_learning_msg__msg__SensorData__fini(msg);
    return false;
  }
  // gyroscope
  if (!geometry_msgs__msg__Vector3__init(&msg->gyroscope)) {
    ros2_learning_msg__msg__SensorData__fini(msg);
    return false;
  }
  // magnetometer
  if (!geometry_msgs__msg__Vector3__init(&msg->magnetometer)) {
    ros2_learning_msg__msg__SensorData__fini(msg);
    return false;
  }
  // pressure
  // depth
  // temperature
  // latitude
  // longitude
  // altitude
  // is_valid
  // confidence
  return true;
}

void
ros2_learning_msg__msg__SensorData__fini(ros2_learning_msg__msg__SensorData * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // acceleration
  geometry_msgs__msg__Vector3__fini(&msg->acceleration);
  // gyroscope
  geometry_msgs__msg__Vector3__fini(&msg->gyroscope);
  // magnetometer
  geometry_msgs__msg__Vector3__fini(&msg->magnetometer);
  // pressure
  // depth
  // temperature
  // latitude
  // longitude
  // altitude
  // is_valid
  // confidence
}

bool
ros2_learning_msg__msg__SensorData__are_equal(const ros2_learning_msg__msg__SensorData * lhs, const ros2_learning_msg__msg__SensorData * rhs)
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
  // acceleration
  if (!geometry_msgs__msg__Vector3__are_equal(
      &(lhs->acceleration), &(rhs->acceleration)))
  {
    return false;
  }
  // gyroscope
  if (!geometry_msgs__msg__Vector3__are_equal(
      &(lhs->gyroscope), &(rhs->gyroscope)))
  {
    return false;
  }
  // magnetometer
  if (!geometry_msgs__msg__Vector3__are_equal(
      &(lhs->magnetometer), &(rhs->magnetometer)))
  {
    return false;
  }
  // pressure
  if (lhs->pressure != rhs->pressure) {
    return false;
  }
  // depth
  if (lhs->depth != rhs->depth) {
    return false;
  }
  // temperature
  if (lhs->temperature != rhs->temperature) {
    return false;
  }
  // latitude
  if (lhs->latitude != rhs->latitude) {
    return false;
  }
  // longitude
  if (lhs->longitude != rhs->longitude) {
    return false;
  }
  // altitude
  if (lhs->altitude != rhs->altitude) {
    return false;
  }
  // is_valid
  if (lhs->is_valid != rhs->is_valid) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  return true;
}

bool
ros2_learning_msg__msg__SensorData__copy(
  const ros2_learning_msg__msg__SensorData * input,
  ros2_learning_msg__msg__SensorData * output)
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
  // acceleration
  if (!geometry_msgs__msg__Vector3__copy(
      &(input->acceleration), &(output->acceleration)))
  {
    return false;
  }
  // gyroscope
  if (!geometry_msgs__msg__Vector3__copy(
      &(input->gyroscope), &(output->gyroscope)))
  {
    return false;
  }
  // magnetometer
  if (!geometry_msgs__msg__Vector3__copy(
      &(input->magnetometer), &(output->magnetometer)))
  {
    return false;
  }
  // pressure
  output->pressure = input->pressure;
  // depth
  output->depth = input->depth;
  // temperature
  output->temperature = input->temperature;
  // latitude
  output->latitude = input->latitude;
  // longitude
  output->longitude = input->longitude;
  // altitude
  output->altitude = input->altitude;
  // is_valid
  output->is_valid = input->is_valid;
  // confidence
  output->confidence = input->confidence;
  return true;
}

ros2_learning_msg__msg__SensorData *
ros2_learning_msg__msg__SensorData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros2_learning_msg__msg__SensorData * msg = (ros2_learning_msg__msg__SensorData *)allocator.allocate(sizeof(ros2_learning_msg__msg__SensorData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ros2_learning_msg__msg__SensorData));
  bool success = ros2_learning_msg__msg__SensorData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ros2_learning_msg__msg__SensorData__destroy(ros2_learning_msg__msg__SensorData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ros2_learning_msg__msg__SensorData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ros2_learning_msg__msg__SensorData__Sequence__init(ros2_learning_msg__msg__SensorData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros2_learning_msg__msg__SensorData * data = NULL;

  if (size) {
    data = (ros2_learning_msg__msg__SensorData *)allocator.zero_allocate(size, sizeof(ros2_learning_msg__msg__SensorData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ros2_learning_msg__msg__SensorData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ros2_learning_msg__msg__SensorData__fini(&data[i - 1]);
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
ros2_learning_msg__msg__SensorData__Sequence__fini(ros2_learning_msg__msg__SensorData__Sequence * array)
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
      ros2_learning_msg__msg__SensorData__fini(&array->data[i]);
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

ros2_learning_msg__msg__SensorData__Sequence *
ros2_learning_msg__msg__SensorData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros2_learning_msg__msg__SensorData__Sequence * array = (ros2_learning_msg__msg__SensorData__Sequence *)allocator.allocate(sizeof(ros2_learning_msg__msg__SensorData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ros2_learning_msg__msg__SensorData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ros2_learning_msg__msg__SensorData__Sequence__destroy(ros2_learning_msg__msg__SensorData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ros2_learning_msg__msg__SensorData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ros2_learning_msg__msg__SensorData__Sequence__are_equal(const ros2_learning_msg__msg__SensorData__Sequence * lhs, const ros2_learning_msg__msg__SensorData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ros2_learning_msg__msg__SensorData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ros2_learning_msg__msg__SensorData__Sequence__copy(
  const ros2_learning_msg__msg__SensorData__Sequence * input,
  ros2_learning_msg__msg__SensorData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ros2_learning_msg__msg__SensorData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ros2_learning_msg__msg__SensorData * data =
      (ros2_learning_msg__msg__SensorData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ros2_learning_msg__msg__SensorData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ros2_learning_msg__msg__SensorData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ros2_learning_msg__msg__SensorData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
