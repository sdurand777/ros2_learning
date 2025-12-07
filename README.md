# ROS2 Learning Workspace

Workspace ROS2 pour apprendre à utiliser ROS2 avec Gazebo Harmonic et ArduSub.

## Structure

```
ros2_learning/
├── ros2_learning_msg/          # Messages custom et exemples pub/sub/services
├── ros2_learning_gazebo/       # Intégration Gazebo Harmonic
├── ros2_learning_ardusub/      # Intégration ArduSub via MAVLink
├── configure_environment.sh    # Configure ~/.bashrc
├── fix_protobuf.sh             # Corrige conflit protobuf
├── PROTOBUF_FIX.md             # Documentation problème protobuf
└── README.md
```

Chaque package a son propre README avec les détails d'utilisation.

## Installation rapide

### 1. Configurer l'environnement

```bash
cd ~/ros2_learning
./configure_environment.sh
source ~/.bashrc
```

### 2. Compiler le workspace

```bash
cd ~/ros2_learning
colcon build
source install/setup.bash
```

### 3. Vérifier l'installation

```bash
# Lister les packages
ros2 pkg list | grep ros2_learning

# Voir les messages custom
ros2 interface show ros2_learning_msg/msg/RobotStatus
```

## Packages

### ros2_learning_msg

Apprendre à créer des **messages** et **services** custom.

```bash
# Publisher / Subscriber
ros2 run ros2_learning_msg publisher_example.py
ros2 run ros2_learning_msg subscriber_example.py

# Services
ros2 run ros2_learning_msg service_server.py
ros2 run ros2_learning_msg service_client.py
```

→ Voir [ros2_learning_msg/README.md](ros2_learning_msg/README.md)

### ros2_learning_gazebo

Utiliser **Gazebo Harmonic** avec ROS2.

```bash
# Installer Gazebo Harmonic
cd ros2_learning_gazebo
./install_gazebo_harmonic.sh

# Lancer la simulation
ros2 launch ros2_learning_gazebo gazebo_sim.launch.py
```

→ Voir [ros2_learning_gazebo/README.md](ros2_learning_gazebo/README.md)

### ros2_learning_ardusub

Communiquer avec **ArduSub** via MAVLink.

```bash
# Mode simulation (sans hardware)
ros2 launch ros2_learning_ardusub ardusub.launch.py simulation:=true

# Avec ArduSub SITL
ros2 launch ros2_learning_ardusub ardusub.launch.py simulation:=false
```

→ Voir [ros2_learning_ardusub/README.md](ros2_learning_ardusub/README.md)

## Scripts d'installation

| Script | Description |
|--------|-------------|
| `configure_environment.sh` | Configure ~/.bashrc (Gazebo, ArduPilot, ROS2) |
| `fix_protobuf.sh` | Corrige le conflit de version protobuf |
| `ros2_learning_gazebo/install_gazebo_harmonic.sh` | Installe Gazebo Harmonic |
| `ros2_learning_ardusub/install_ardusub_sitl.sh` | Installe ArduPilot SITL |
| `ros2_learning_ardusub/setup_ardusub_gazebo.sh` | Configure ArduSub + Gazebo |

## Problème protobuf

Si tu rencontres des erreurs de compilation avec `gz::msgs::Sensor has incomplete type`:

```bash
# Diagnostic
which protoc
protoc --version  # Doit être 3.12.4

# Si version 25.x, exécuter:
./fix_protobuf.sh
```

→ Voir [PROTOBUF_FIX.md](PROTOBUF_FIX.md)

## Topics principaux

| Topic | Type | Package | Description |
|-------|------|---------|-------------|
| `/robot_status` | RobotStatus | msg | État du robot |
| `/sensor_data` | SensorData | msg | Données capteurs |
| `/cmd_vel` | Twist | gazebo/ardusub | Commandes vitesse |
| `/odom` | Odometry | gazebo/ardusub | Odométrie |
| `/depth` | Float64 | ardusub | Profondeur |
| `/imu/data` | Imu | gazebo/ardusub | Données IMU |

## Services principaux

| Service | Type | Package | Description |
|---------|------|---------|-------------|
| `/get_robot_status` | GetStatus | msg | Obtenir état robot |
| `/set_robot_command` | SetCommand | msg | Envoyer commande |
| `/arm` | SetBool | ardusub | Armer/désarmer |

## Commandes utiles

```bash
# Lister les topics
ros2 topic list

# Écouter un topic
ros2 topic echo /robot_status

# Publier sur un topic
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}}"

# Lister les services
ros2 service list

# Appeler un service
ros2 service call /arm std_srvs/srv/SetBool "{data: true}"

# Lancer Gazebo
gz sim

# Voir les topics Gazebo
gz topic -l
```

## Architecture complète (ArduSub + Gazebo + ROS2)

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   ArduSub SITL  │────▶│ ardupilot_gazebo│────▶│  Gazebo Harmonic│
│   (Firmware)    │     │    (Plugin)     │     │   (Simulation)  │
└────────┬────────┘     └─────────────────┘     └────────┬────────┘
         │                                               │
         │ MAVLink (UDP 14550)                          │ gz topics
         │                                               │
         ▼                                               ▼
┌─────────────────┐                            ┌─────────────────┐
│ ros2_learning   │                            │   ros_gz_bridge │
│    _ardusub     │                            │                 │
└────────┬────────┘                            └────────┬────────┘
         │                                               │
         │ ROS2 topics                                  │ ROS2 topics
         │                                               │
         └───────────────────┬───────────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Ton code ROS2 │
                    └─────────────────┘
```
# ros2_learning
