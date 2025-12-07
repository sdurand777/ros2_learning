# Request - Send command to robot
string robot_name
uint8 command_type
float32[] parameters

# Command type constants
uint8 CMD_ARM=0
uint8 CMD_DISARM=1
uint8 CMD_SET_MODE=2
uint8 CMD_SET_DEPTH=3
uint8 CMD_SET_HEADING=4
uint8 CMD_MOVE=5
