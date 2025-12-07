# Custom message for sensor data
std_msgs/Header header

# IMU data
geometry_msgs/Vector3 acceleration
geometry_msgs/Vector3 gyroscope
geometry_msgs/Vector3 magnetometer

# Pressure/Depth sensor
float32 pressure      # in Pascals
float32 depth         # in meters
float32 temperature   # in Celsius

# GPS (if available at surface)
float64 latitude
float64 longitude
float32 altitude

# Data quality
bool is_valid
float32 confidence    # 0.0 to 1.0
