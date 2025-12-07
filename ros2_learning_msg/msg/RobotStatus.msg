# Custom message for robot status
std_msgs/Header header

# Robot identification
string robot_name
uint32 robot_id

# Position (x, y, z)
geometry_msgs/Point position

# Orientation (quaternion)
geometry_msgs/Quaternion orientation

# Velocity (linear and angular)
geometry_msgs/Twist velocity

# Battery level (0-100%)
float32 battery_level

# Status flags
bool is_armed
bool is_connected
uint8 mode

# Mode constants
uint8 MODE_MANUAL=0
uint8 MODE_STABILIZE=1
uint8 MODE_DEPTH_HOLD=2
uint8 MODE_AUTO=3
