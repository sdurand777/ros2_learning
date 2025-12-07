#!/bin/bash
# ==============================================================================
# Script de configuration ArduSub avec Gazebo Harmonic
# ==============================================================================
#
# Ce script configure l'environnement pour utiliser ArduSub avec Gazebo Harmonic
# via le plugin ardupilot_gazebo.
#
# Prérequis:
# - Gazebo Harmonic installé
# - ArduPilot compilé pour SITL
# - ROS2 avec ros_gz installé
#
# Usage: ./setup_ardusub_gazebo.sh
# ==============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║       Configuration ArduSub + Gazebo Harmonic                 ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"

# ==============================================================================
# Step 1: Install ardupilot_gazebo plugin
# ==============================================================================
echo -e "\n${BLUE}[1/4] Installation du plugin ardupilot_gazebo...${NC}"

PLUGIN_DIR="$HOME/ardupilot_gazebo"

if [ -d "$PLUGIN_DIR" ]; then
    echo -e "${YELLOW}Plugin existe déjà, mise à jour...${NC}"
    cd "$PLUGIN_DIR"
    git pull origin main || true
else
    cd "$HOME"
    git clone https://github.com/ArduPilot/ardupilot_gazebo.git
    cd "$PLUGIN_DIR"
fi

# Build the plugin
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

echo -e "${GREEN}Plugin compilé!${NC}"

# ==============================================================================
# Step 2: Setup environment variables
# ==============================================================================
echo -e "\n${BLUE}[2/4] Configuration des variables d'environnement...${NC}"

# Add plugin paths to bashrc
if ! grep -q "ardupilot_gazebo" ~/.bashrc; then
    echo "" >> ~/.bashrc
    echo "# ArduPilot Gazebo Plugin" >> ~/.bashrc
    echo "export GZ_SIM_SYSTEM_PLUGIN_PATH=\"\$HOME/ardupilot_gazebo/build:\$GZ_SIM_SYSTEM_PLUGIN_PATH\"" >> ~/.bashrc
    echo "export GZ_SIM_RESOURCE_PATH=\"\$HOME/ardupilot_gazebo/models:\$HOME/ardupilot_gazebo/worlds:\$GZ_SIM_RESOURCE_PATH\"" >> ~/.bashrc
    echo -e "${GREEN}Variables d'environnement ajoutées à ~/.bashrc${NC}"
fi

# Export for current session
export GZ_SIM_SYSTEM_PLUGIN_PATH="$HOME/ardupilot_gazebo/build:$GZ_SIM_SYSTEM_PLUGIN_PATH"
export GZ_SIM_RESOURCE_PATH="$HOME/ardupilot_gazebo/models:$HOME/ardupilot_gazebo/worlds:$GZ_SIM_RESOURCE_PATH"

# ==============================================================================
# Step 3: Create BlueROV2 model for Gazebo
# ==============================================================================
echo -e "\n${BLUE}[3/4] Création du modèle BlueROV2...${NC}"

MODEL_DIR="$HOME/ardupilot_gazebo/models/bluerov2_heavy"
mkdir -p "$MODEL_DIR"

cat > "$MODEL_DIR/model.config" << 'EOF'
<?xml version="1.0"?>
<model>
  <name>BlueROV2 Heavy</name>
  <version>1.0</version>
  <sdf version="1.8">model.sdf</sdf>
  <author>
    <name>ROS2 Learning</name>
  </author>
  <description>
    BlueROV2 Heavy model for ArduSub SITL with Gazebo
  </description>
</model>
EOF

cat > "$MODEL_DIR/model.sdf" << 'EOF'
<?xml version="1.0"?>
<sdf version="1.8">
  <model name="bluerov2_heavy">
    <pose>0 0 -1 0 0 0</pose>

    <link name="base_link">
      <inertial>
        <mass>11.5</mass>
        <inertia>
          <ixx>0.16</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>0.16</iyy>
          <iyz>0</iyz>
          <izz>0.16</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <box>
            <size>0.457 0.338 0.254</size>
          </box>
        </geometry>
      </collision>

      <visual name="visual">
        <geometry>
          <box>
            <size>0.457 0.338 0.254</size>
          </box>
        </geometry>
        <material>
          <ambient>0.0 0.2 0.6 1</ambient>
          <diffuse>0.0 0.3 0.8 1</diffuse>
        </material>
      </visual>

      <!-- IMU Sensor -->
      <sensor name="imu" type="imu">
        <always_on>true</always_on>
        <update_rate>200</update_rate>
        <topic>imu</topic>
      </sensor>
    </link>

    <!-- ArduPilot plugin -->
    <plugin filename="ArduPilotPlugin" name="ardupilot_gazebo::ArduPilotPlugin">
      <fdm_addr>127.0.0.1</fdm_addr>
      <fdm_port_in>9002</fdm_port_in>
      <connectionTimeoutMaxCount>5</connectionTimeoutMaxCount>
      <lock_step>1</lock_step>

      <modelXYZToAirplaneXForwardZDown>0 0 0 3.141593 0 0</modelXYZToAirplaneXForwardZDown>
      <gazeboXYZToNED>0 0 0 3.141593 0 0</gazeboXYZToNED>

      <imuName>imu</imuName>

      <!-- 8 thrusters for BlueROV2 Heavy -->
      <!-- Horizontal thrusters (vectored) -->
      <control channel="0">
        <jointName>thruster_0_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <cmd_topic>/model/bluerov2_heavy/joint/thruster_0_joint/cmd_thrust</cmd_topic>
        <multiplier>1000</multiplier>
      </control>

      <control channel="1">
        <jointName>thruster_1_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>

      <control channel="2">
        <jointName>thruster_2_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>

      <control channel="3">
        <jointName>thruster_3_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>

      <!-- Vertical thrusters -->
      <control channel="4">
        <jointName>thruster_4_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>

      <control channel="5">
        <jointName>thruster_5_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>

      <control channel="6">
        <jointName>thruster_6_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>

      <control channel="7">
        <jointName>thruster_7_joint</jointName>
        <servo_min>1100</servo_min>
        <servo_max>1900</servo_max>
        <type>VELOCITY</type>
        <multiplier>1000</multiplier>
      </control>
    </plugin>

    <!-- Buoyancy plugin -->
    <plugin filename="gz-sim-buoyancy-system" name="gz::sim::systems::Buoyancy">
      <uniform_fluid_density>1025</uniform_fluid_density>
    </plugin>

    <!-- Hydrodynamics plugin -->
    <plugin filename="gz-sim-hydrodynamics-system" name="gz::sim::systems::Hydrodynamics">
      <link_name>base_link</link_name>
      <xDotU>-4.876</xDotU>
      <yDotV>-126.324</yDotV>
      <zDotW>-126.324</zDotW>
      <kDotP>-0.0135</kDotP>
      <mDotQ>-0.0135</mDotQ>
      <nDotR>-0.0135</nDotR>
      <xU>-6.2282</xU>
      <yV>-6.2282</yV>
      <zW>-6.2282</zW>
      <kP>-0.1916</kP>
      <mQ>-0.1916</mQ>
      <nR>-0.1916</nR>
    </plugin>

  </model>
</sdf>
EOF

echo -e "${GREEN}Modèle BlueROV2 créé!${NC}"

# ==============================================================================
# Step 4: Create launch scripts
# ==============================================================================
echo -e "\n${BLUE}[4/4] Création des scripts de lancement...${NC}"

# Script to launch full simulation
cat > "$HOME/launch_ardusub_gazebo.sh" << 'EOF'
#!/bin/bash
# Launch ArduSub SITL with Gazebo Harmonic

# Terminal 1: Start Gazebo
echo "Starting Gazebo..."
gz sim ~/ardupilot_gazebo/worlds/underwater.sdf &
GAZEBO_PID=$!
sleep 5

# Terminal 2: Start ArduSub SITL
echo "Starting ArduSub SITL..."
cd ~/ardupilot/ArduSub
../Tools/autotest/sim_vehicle.py -v ArduSub -f gazebo-bluerov2 --model JSON --speedup 1 &
ARDUSUB_PID=$!
sleep 5

# Terminal 3: Start MAVProxy (optional)
echo "Starting MAVProxy..."
mavproxy.py --master=127.0.0.1:14550 --out=udp:127.0.0.1:14551 &
MAVPROXY_PID=$!

echo ""
echo "=== Simulation Started ==="
echo "Gazebo PID: $GAZEBO_PID"
echo "ArduSub PID: $ARDUSUB_PID"
echo "MAVProxy PID: $MAVPROXY_PID"
echo ""
echo "Press Ctrl+C to stop all processes"

# Wait and cleanup
trap "kill $GAZEBO_PID $ARDUSUB_PID $MAVPROXY_PID 2>/dev/null" EXIT
wait
EOF

chmod +x "$HOME/launch_ardusub_gazebo.sh"

# Create underwater world if not exists
WORLD_DIR="$HOME/ardupilot_gazebo/worlds"
mkdir -p "$WORLD_DIR"

if [ ! -f "$WORLD_DIR/underwater.sdf" ]; then
    cat > "$WORLD_DIR/underwater.sdf" << 'EOF'
<?xml version="1.0"?>
<sdf version="1.8">
  <world name="underwater_world">
    <physics name="1ms" type="dart">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>

    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics"/>
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors"/>
    <plugin filename="gz-sim-user-commands-system" name="gz::sim::systems::UserCommands"/>
    <plugin filename="gz-sim-scene-broadcaster-system" name="gz::sim::systems::SceneBroadcaster"/>
    <plugin filename="gz-sim-imu-system" name="gz::sim::systems::Imu"/>
    <plugin filename="gz-sim-buoyancy-system" name="gz::sim::systems::Buoyancy">
      <uniform_fluid_density>1025</uniform_fluid_density>
    </plugin>

    <scene>
      <ambient>0.2 0.3 0.5 1</ambient>
      <background>0.1 0.2 0.4 1</background>
    </scene>

    <light type="directional" name="sun">
      <pose>0 0 100 0 0 0</pose>
      <diffuse>0.5 0.6 0.7 1</diffuse>
    </light>

    <model name="sea_floor">
      <static>true</static>
      <pose>0 0 -20 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane><normal>0 0 1</normal><size>100 100</size></plane>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <plane><normal>0 0 1</normal><size>100 100</size></plane>
          </geometry>
          <material>
            <ambient>0.4 0.35 0.25 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <include>
      <uri>model://bluerov2_heavy</uri>
      <pose>0 0 -2 0 0 0</pose>
    </include>

  </world>
</sdf>
EOF
fi

# ==============================================================================
# Summary
# ==============================================================================
echo -e "\n${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║               Configuration terminée!                          ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"

echo -e "\n${BLUE}Éléments configurés:${NC}"
echo "  - Plugin ardupilot_gazebo compilé"
echo "  - Modèle BlueROV2 Heavy créé"
echo "  - World underwater créé"
echo "  - Script de lancement créé"

echo -e "\n${BLUE}Pour lancer la simulation complète:${NC}"
echo "  ~/launch_ardusub_gazebo.sh"

echo -e "\n${BLUE}Pour lancer les composants séparément:${NC}"
echo "  Terminal 1: gz sim ~/ardupilot_gazebo/worlds/underwater.sdf"
echo "  Terminal 2: cd ~/ardupilot && Tools/autotest/sim_vehicle.py -v ArduSub"
echo "  Terminal 3: ros2 launch ros2_learning_ardusub ardusub.launch.py"

echo -e "\n${YELLOW}Redémarrez votre terminal pour charger les variables d'environnement.${NC}"
