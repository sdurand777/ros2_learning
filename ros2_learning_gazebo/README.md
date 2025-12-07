# ros2_learning_gazebo

Package ROS2 pour apprendre à utiliser **Gazebo Harmonic** avec ROS2.

## Prérequis

Installer Gazebo Harmonic:
```bash
./install_gazebo_harmonic.sh
```

## Contenu

```
ros2_learning_gazebo/
├── scripts/
│   ├── gazebo_bridge_node.py   # Configuration du bridge ROS-Gazebo
│   ├── model_spawner.py        # Spawn de modèles dans Gazebo
│   ├── pose_publisher.py       # Publie la pose du robot + TF
│   ├── velocity_controller.py  # Contrôle clavier du robot
│   └── sensor_reader.py        # Lecture des capteurs Gazebo
├── launch/
│   └── gazebo_sim.launch.py    # Launch file complet
├── config/
│   ├── bridge_config.yaml      # Configuration ros_gz_bridge
│   └── worlds/
│       └── underwater.sdf      # Monde sous-marin
└── install_gazebo_harmonic.sh  # Script d'installation
```

## Compilation

```bash
cd ~/ros2_learning
colcon build --packages-select ros2_learning_gazebo
source install/setup.bash
```

## Utilisation

### Lancer Gazebo seul

```bash
# Monde par défaut
gz sim

# Monde underwater
gz sim ~/ros2_learning/ros2_learning_gazebo/config/worlds/underwater.sdf
```

### Lancer avec ROS2 (launch file)

```bash
ros2 launch ros2_learning_gazebo gazebo_sim.launch.py
```

Options:
```bash
ros2 launch ros2_learning_gazebo gazebo_sim.launch.py \
    world:=underwater_world \
    robot_name:=bluerov2 \
    use_sim_time:=true
```

### Scripts individuels

```bash
# Bridge ROS-Gazebo (affiche les commandes de bridge)
ros2 run ros2_learning_gazebo gazebo_bridge_node.py

# Spawner de modèles
ros2 run ros2_learning_gazebo model_spawner.py --ros-args \
    -p world_name:=underwater_world \
    -p model_name:=test_box \
    -p x:=0.0 -p y:=0.0 -p z:=-2.0

# Publisher de pose
ros2 run ros2_learning_gazebo pose_publisher.py --ros-args \
    -p robot_name:=bluerov2

# Contrôle clavier
ros2 run ros2_learning_gazebo velocity_controller.py

# Lecteur de capteurs
ros2 run ros2_learning_gazebo sensor_reader.py
```

### Bridge ROS-Gazebo manuel

```bash
# Bridge pour cmd_vel (ROS → Gazebo)
ros2 run ros_gz_bridge parameter_bridge \
    /model/bluerov2/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist

# Bridge pour odometry (Gazebo → ROS)
ros2 run ros_gz_bridge parameter_bridge \
    /model/bluerov2/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry

# Bridge avec fichier de config
ros2 run ros_gz_bridge parameter_bridge --ros-args \
    -p config_file:=$(ros2 pkg prefix ros2_learning_gazebo)/share/ros2_learning_gazebo/config/bridge_config.yaml
```

## Contrôle clavier (velocity_controller.py)

| Touche | Action |
|--------|--------|
| W/S | Avancer / Reculer |
| A/D | Gauche / Droite |
| Q/E | Monter / Descendre |
| J/L | Rotation gauche / droite (yaw) |
| I/K | Pitch up / down |
| U/O | Roll gauche / droite |
| Space | Stop |
| Ctrl+C | Quitter |

## Topics

| Topic | Type | Direction | Description |
|-------|------|-----------|-------------|
| /cmd_vel | Twist | ROS → GZ | Commandes de vitesse |
| /odom | Odometry | GZ → ROS | Odométrie |
| /imu/data | Imu | GZ → ROS | Données IMU |
| /camera/image_raw | Image | GZ → ROS | Image caméra |
| /depth | Float64 | GZ → ROS | Profondeur |
| /bluerov2/pose | PoseStamped | ROS | Pose du robot |

## Commandes Gazebo utiles

```bash
# Lister les topics Gazebo
gz topic -l

# Écouter un topic Gazebo
gz topic -e -t /model/bluerov2/odometry

# Publier sur un topic Gazebo
gz topic -t /model/bluerov2/cmd_vel -m gz.msgs.Twist -p 'linear: {x: 1.0}'

# Lister les modèles
gz model --list

# Info sur un modèle
gz model -m bluerov2

# Pause/Resume simulation
gz service -s /world/underwater_world/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --req 'pause: true'
```

## Création de mondes

Les fichiers SDF sont dans `config/worlds/`. Structure d'un monde:

```xml
<?xml version="1.0"?>
<sdf version="1.8">
  <world name="my_world">
    <!-- Plugins requis -->
    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics"/>
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors"/>

    <!-- Lumière -->
    <light type="directional" name="sun">...</light>

    <!-- Modèles -->
    <model name="ground">...</model>

    <!-- Include d'autres modèles -->
    <include>
      <uri>model://bluerov2</uri>
      <pose>0 0 -2 0 0 0</pose>
    </include>
  </world>
</sdf>
```
