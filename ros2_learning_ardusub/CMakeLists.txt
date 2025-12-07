cmake_minimum_required(VERSION 3.8)
project(ros2_learning_ardusub)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

# Install Python scripts
install(PROGRAMS
  scripts/ardusub_node.py
  scripts/mavlink_bridge.py
  scripts/thruster_controller.py
  scripts/depth_controller.py
  scripts/heading_controller.py
  scripts/telemetry_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files and config
install(DIRECTORY
  launch
  config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
