# ros2_learning_msg

Package ROS2 pour apprendre à créer des **messages custom** et des **services** avec des exemples Python.

## Contenu

```
ros2_learning_msg/
├── msg/
│   ├── RobotStatus.msg      # État du robot (position, orientation, batterie, mode)
│   └── SensorData.msg       # Données capteurs (IMU, pression, GPS)
├── srv/
│   ├── GetStatus.srv        # Service pour obtenir l'état d'un robot
│   └── SetCommand.srv       # Service pour envoyer des commandes
└── scripts/
    ├── publisher_example.py  # Publie RobotStatus et SensorData
    ├── subscriber_example.py # S'abonne aux topics
    ├── service_server.py     # Serveur de services
    └── service_client.py     # Client de services
```

## Compilation

```bash
cd ~/ros2_learning
colcon build --packages-select ros2_learning_msg
source install/setup.bash
```

## Utilisation

### Publisher / Subscriber

```bash
# Terminal 1: Lancer le publisher
ros2 run ros2_learning_msg publisher_example.py

# Terminal 2: Lancer le subscriber
ros2 run ros2_learning_msg subscriber_example.py
```

### Services

```bash
# Terminal 1: Lancer le serveur
ros2 run ros2_learning_msg service_server.py

# Terminal 2: Lancer le client (exécute des commandes de test)
ros2 run ros2_learning_msg service_client.py
```

### Inspecter les messages

```bash
# Voir la définition d'un message
ros2 interface show ros2_learning_msg/msg/RobotStatus

# Voir la définition d'un service
ros2 interface show ros2_learning_msg/srv/GetStatus

# Lister les topics actifs
ros2 topic list

# Écouter un topic
ros2 topic echo /robot_status
```

### Appeler un service manuellement

```bash
# Obtenir le status d'un robot
ros2 service call /get_robot_status ros2_learning_msg/srv/GetStatus "{robot_name: 'bluerov2'}"

# Armer un robot
ros2 service call /set_robot_command ros2_learning_msg/srv/SetCommand "{robot_name: 'bluerov2', command_type: 0, parameters: []}"
```

## Messages

### RobotStatus.msg

| Champ | Type | Description |
|-------|------|-------------|
| header | std_msgs/Header | Timestamp et frame |
| robot_name | string | Nom du robot |
| robot_id | uint32 | ID unique |
| position | geometry_msgs/Point | Position x, y, z |
| orientation | geometry_msgs/Quaternion | Orientation |
| velocity | geometry_msgs/Twist | Vitesse linéaire/angulaire |
| battery_level | float32 | Niveau batterie (0-100%) |
| is_armed | bool | Robot armé |
| is_connected | bool | Connexion active |
| mode | uint8 | Mode de vol (MANUAL=0, STABILIZE=1, DEPTH_HOLD=2, AUTO=3) |

### SensorData.msg

| Champ | Type | Description |
|-------|------|-------------|
| acceleration | Vector3 | Accéléromètre (m/s²) |
| gyroscope | Vector3 | Gyroscope (rad/s) |
| magnetometer | Vector3 | Magnétomètre |
| pressure | float32 | Pression (Pa) |
| depth | float32 | Profondeur (m) |
| temperature | float32 | Température (°C) |
| latitude/longitude | float64 | GPS |
| is_valid | bool | Données valides |
| confidence | float32 | Confiance (0-1) |

## Services

### GetStatus.srv

**Request:** `robot_name` (string)
**Response:** `success`, `message`, `status` (RobotStatus)

### SetCommand.srv

**Request:** `robot_name`, `command_type`, `parameters[]`
**Response:** `success`, `message`, `command_id`

Types de commandes:
- `CMD_ARM = 0`
- `CMD_DISARM = 1`
- `CMD_SET_MODE = 2`
- `CMD_SET_DEPTH = 3`
- `CMD_SET_HEADING = 4`
- `CMD_MOVE = 5`
