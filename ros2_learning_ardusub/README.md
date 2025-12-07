# ros2_learning_ardusub

Package ROS2 pour communiquer avec **ArduSub** via MAVLink/MAVROS.

## Prérequis

### Option 1: ArduSub SITL (simulation)
```bash
./install_ardusub_sitl.sh
```

### Option 2: ArduSub + Gazebo
```bash
# Après avoir compilé ardupilot_gazebo
./setup_ardusub_gazebo.sh
```

### Dépendances ROS2
```bash
sudo apt install ros-${ROS_DISTRO}-mavros ros-${ROS_DISTRO}-mavros-msgs
```

## Contenu

```
ros2_learning_ardusub/
├── scripts/
│   ├── ardusub_node.py         # Node principal (connexion MAVLink)
│   ├── mavlink_bridge.py       # Bridge MAVLink ↔ ROS2
│   ├── thruster_controller.py  # Contrôle des thrusters
│   ├── depth_controller.py     # PID pour maintien de profondeur
│   ├── heading_controller.py   # PID pour maintien de cap
│   └── telemetry_publisher.py  # Télémétrie simulée (sans hardware)
├── launch/
│   └── ardusub.launch.py       # Launch file
├── config/
│   ├── ardusub_params.yaml     # Paramètres connexion
│   ├── depth_controller.yaml   # Gains PID profondeur
│   └── heading_controller.yaml # Gains PID cap
├── install_ardusub_sitl.sh     # Installation ArduPilot SITL
└── setup_ardusub_gazebo.sh     # Configuration avec Gazebo
```

## Compilation

```bash
cd ~/ros2_learning
colcon build --packages-select ros2_learning_ardusub
source install/setup.bash
```

## Utilisation

### Mode simulation (sans hardware)

```bash
# Lance tous les nodes avec télémétrie simulée
ros2 launch ros2_learning_ardusub ardusub.launch.py simulation:=true
```

### Avec ArduSub SITL

```bash
# Terminal 1: Lancer ArduSub SITL
cd ~/ardupilot/ArduSub
../Tools/autotest/sim_vehicle.py -v ArduSub --console --map

# Terminal 2: Lancer les nodes ROS2
ros2 launch ros2_learning_ardusub ardusub.launch.py simulation:=false
```

### Avec ArduSub + Gazebo

```bash
# Terminal 1: Gazebo
gz sim ~/ardupilot_gazebo/worlds/underwater.sdf

# Terminal 2: ArduSub SITL
cd ~/ardupilot/ArduSub
../Tools/autotest/sim_vehicle.py -v ArduSub -f gazebo-bluerov2 --model JSON

# Terminal 3: ROS2
ros2 launch ros2_learning_ardusub ardusub.launch.py simulation:=false
```

### Scripts individuels

```bash
# Node principal ArduSub
ros2 run ros2_learning_ardusub ardusub_node.py --ros-args \
    -p connection_string:="udpin:0.0.0.0:14550"

# Télémétrie simulée
ros2 run ros2_learning_ardusub telemetry_publisher.py

# Contrôleur de thrusters
ros2 run ros2_learning_ardusub thruster_controller.py

# Contrôleur de profondeur
ros2 run ros2_learning_ardusub depth_controller.py

# Contrôleur de cap
ros2 run ros2_learning_ardusub heading_controller.py
```

## Topics

### Télémétrie (sortie)

| Topic | Type | Description |
|-------|------|-------------|
| /odom | Odometry | Odométrie |
| /pose | PoseStamped | Position et orientation |
| /imu/data | Imu | Données IMU |
| /depth | Float64 | Profondeur (m) |
| /heading | Float64 | Cap (rad) |
| /battery | BatteryState | État batterie |
| /armed | Bool | État armé |
| /mode | UInt8 | Mode de vol |

### Commandes (entrée)

| Topic | Type | Description |
|-------|------|-------------|
| /cmd_vel | Twist | Vitesse désirée |
| /cmd_wrench | Wrench | Force/couple désiré |
| /depth/target | Float64 | Profondeur cible |
| /depth/enable | Bool | Activer contrôle profondeur |
| /heading/target | Float64 | Cap cible (rad) |
| /heading/enable | Bool | Activer contrôle cap |

### Thrusters

| Topic | Type | Description |
|-------|------|-------------|
| /thrusters/pwm | UInt16MultiArray | Valeurs PWM (1100-1900) |
| /thrusters/thrust | Float64MultiArray | Forces (N) |

## Services

| Service | Type | Description |
|---------|------|-------------|
| /arm | SetBool | Armer (true) / Désarmer (false) |
| /dive | Trigger | Plonger |
| /surface | Trigger | Remonter en surface |

### Exemples d'appels

```bash
# Armer le robot
ros2 service call /arm std_srvs/srv/SetBool "{data: true}"

# Désarmer
ros2 service call /arm std_srvs/srv/SetBool "{data: false}"

# Définir profondeur cible
ros2 topic pub /depth/target std_msgs/msg/Float64 "{data: 5.0}"

# Activer le contrôle de profondeur
ros2 topic pub /depth/enable std_msgs/msg/Bool "{data: true}"

# Envoyer une commande de vitesse
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {z: 0.1}}"
```

## Modes ArduSub

| ID | Mode | Description |
|----|------|-------------|
| 0 | STABILIZE | Stabilisation d'attitude |
| 2 | ALT_HOLD | Maintien d'altitude |
| 4 | GUIDED | Contrôle externe |
| 7 | SURFACE | Remontée en surface |
| 9 | POSHOLD | Maintien de position |
| 16 | MANUAL | Contrôle manuel |
| 19 | DEPTH_HOLD | Maintien de profondeur |

## Configuration des PID

### Profondeur (depth_controller.yaml)
```yaml
depth_controller:
  ros__parameters:
    kp: 50.0      # Gain proportionnel
    ki: 5.0       # Gain intégral
    kd: 20.0      # Gain dérivé
    max_thrust: 100.0
    dead_band: 0.05  # Bande morte (m)
```

### Cap (heading_controller.yaml)
```yaml
heading_controller:
  ros__parameters:
    kp: 10.0
    ki: 1.0
    kd: 5.0
    max_torque: 20.0
    dead_band: 0.02  # ~1 degré
```

## BlueROV2 Thrusters

```
    Front
  1       2      ← Horizontal vectored
     \ /
      X
     / \
  4       3      ← Horizontal vectored

  5       6      ← Vertical
     [_]
  7       8      ← Vertical
    Back
```

| Canal | Position | Direction |
|-------|----------|-----------|
| 0 | Front-right | Forward-right |
| 1 | Front-left | Forward-left |
| 2 | Rear-right | Forward-left |
| 3 | Rear-left | Forward-right |
| 4 | Vertical front-right | Up |
| 5 | Vertical front-left | Up |
| 6 | Vertical rear-right | Up |
| 7 | Vertical rear-left | Up |

## Connexion MAVLink

```bash
# UDP (défaut SITL)
connection_string: "udpin:0.0.0.0:14550"

# TCP
connection_string: "tcp:192.168.2.1:5760"

# Serial
connection_string: "/dev/ttyACM0"
```
