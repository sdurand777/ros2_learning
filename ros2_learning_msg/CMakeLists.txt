cmake_minimum_required(VERSION 3.8)
project(ros2_learning_msg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate custom messages and services
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotStatus.msg"
  "msg/SensorData.msg"
  "srv/GetStatus.srv"
  "srv/SetCommand.srv"
  DEPENDENCIES std_msgs geometry_msgs sensor_msgs
)

# Install Python scripts
install(PROGRAMS
  scripts/publisher_example.py
  scripts/subscriber_example.py
  scripts/service_server.py
  scripts/service_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
