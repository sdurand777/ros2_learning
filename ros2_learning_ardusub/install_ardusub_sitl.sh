#!/bin/bash
# ==============================================================================
# Script d'installation d'ArduSub SITL (Software In The Loop) avec Gazebo
# ==============================================================================
#
# Ce script installe:
# - ArduPilot (avec ArduSub)
# - SITL dependencies
# - pymavlink
# - MAVROS pour ROS2
#
# Usage: ./install_ardusub_sitl.sh
# ==============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║          Installation ArduSub SITL + Gazebo                   ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo -e "${RED}Ne pas exécuter en tant que root.${NC}"
    exit 1
fi

# Detect ROS2 distribution
if [ -n "$ROS_DISTRO" ]; then
    ROS_VERSION=$ROS_DISTRO
    echo -e "${GREEN}ROS2 distribution: $ROS_VERSION${NC}"
else
    echo -e "${YELLOW}ROS_DISTRO non défini. Utilisation de 'humble'.${NC}"
    ROS_VERSION="humble"
fi

# ==============================================================================
# Step 1: Install system dependencies
# ==============================================================================
echo -e "\n${BLUE}[1/6] Installation des dépendances système...${NC}"

sudo apt-get update
sudo apt-get install -y \
    git \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    gcc \
    g++ \
    cmake \
    build-essential

# ==============================================================================
# Step 2: Install Python dependencies
# ==============================================================================
echo -e "\n${BLUE}[2/6] Installation des dépendances Python...${NC}"

pip3 install --user \
    pymavlink \
    mavproxy \
    pexpect \
    future \
    lxml \
    numpy \
    empy==3.3.4 \
    pyserial \
    dronecan \
    scipy

# Add local bin to PATH
if ! grep -q ".local/bin" ~/.bashrc; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
fi
export PATH="$HOME/.local/bin:$PATH"

# ==============================================================================
# Step 3: Clone ArduPilot
# ==============================================================================
echo -e "\n${BLUE}[3/6] Clonage d'ArduPilot...${NC}"

ARDUPILOT_DIR="$HOME/ardupilot"

if [ -d "$ARDUPILOT_DIR" ]; then
    echo -e "${YELLOW}ArduPilot existe déjà dans $ARDUPILOT_DIR${NC}"
    cd "$ARDUPILOT_DIR"
    git fetch origin
    git pull origin master || true
else
    cd "$HOME"
    git clone --recursive https://github.com/ArduPilot/ardupilot.git
    cd ardupilot
fi

# Update submodules
git submodule update --init --recursive

# ==============================================================================
# Step 4: Install ArduPilot prerequisites
# ==============================================================================
echo -e "\n${BLUE}[4/6] Installation des prérequis ArduPilot...${NC}"

cd "$ARDUPILOT_DIR"

# Run the prerequisite installer
Tools/environment_install/install-prereqs-ubuntu.sh -y || true

# Reload profile
source ~/.profile || true

# ==============================================================================
# Step 5: Install MAVROS for ROS2
# ==============================================================================
echo -e "\n${BLUE}[5/6] Installation de MAVROS pour ROS2...${NC}"

sudo apt-get install -y \
    ros-${ROS_VERSION}-mavros \
    ros-${ROS_VERSION}-mavros-msgs \
    ros-${ROS_VERSION}-mavros-extras

# Install GeographicLib datasets
echo -e "${YELLOW}Installation des datasets GeographicLib...${NC}"
sudo /opt/ros/${ROS_VERSION}/lib/mavros/install_geographiclib_datasets.sh || true

# ==============================================================================
# Step 6: Build ArduSub SITL
# ==============================================================================
echo -e "\n${BLUE}[6/6] Compilation ArduSub SITL...${NC}"

cd "$ARDUPILOT_DIR"

# Configure and build ArduSub for SITL
./waf configure --board sitl
./waf sub

echo -e "${GREEN}ArduSub SITL compilé avec succès!${NC}"

# ==============================================================================
# Create helper scripts
# ==============================================================================
echo -e "\n${BLUE}Création des scripts helper...${NC}"

# Script to start ArduSub SITL
cat > "$HOME/start_ardusub_sitl.sh" << 'EOF'
#!/bin/bash
# Start ArduSub SITL simulation

cd ~/ardupilot/ArduSub

# Default parameters
LOCATION="33.810313,-118.393867,0,270"  # Long Beach, CA
SPEEDUP=1
FRAME="vectored"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --gazebo)
            USE_GAZEBO=1
            shift
            ;;
        --speedup)
            SPEEDUP="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

# Build command
CMD="../Tools/autotest/sim_vehicle.py -v ArduSub -f $FRAME --speedup $SPEEDUP"

if [ "$USE_GAZEBO" = "1" ]; then
    CMD="$CMD --add-param-file=../Tools/autotest/default_params/gazebo-iris.parm"
fi

echo "Starting ArduSub SITL..."
echo "Command: $CMD"

$CMD
EOF

chmod +x "$HOME/start_ardusub_sitl.sh"

# Script to connect with mavproxy
cat > "$HOME/connect_mavproxy.sh" << 'EOF'
#!/bin/bash
# Connect to ArduSub SITL with MAVProxy

mavproxy.py --master=udpin:0.0.0.0:14550 \
            --out=udp:127.0.0.1:14551 \
            --out=udp:127.0.0.1:14552
EOF

chmod +x "$HOME/connect_mavproxy.sh"

# ==============================================================================
# Environment setup
# ==============================================================================
echo -e "\n${BLUE}Configuration de l'environnement...${NC}"

# Add ArduPilot to PATH
if ! grep -q "ardupilot" ~/.bashrc; then
    echo "" >> ~/.bashrc
    echo "# ArduPilot environment" >> ~/.bashrc
    echo "export PATH=\"\$HOME/ardupilot/Tools/autotest:\$PATH\"" >> ~/.bashrc
fi

# ==============================================================================
# Summary
# ==============================================================================
echo -e "\n${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║               Installation terminée!                          ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"

echo -e "\n${BLUE}Packages installés:${NC}"
echo "  - ArduPilot (ArduSub SITL) dans $ARDUPILOT_DIR"
echo "  - pymavlink, mavproxy"
echo "  - ros-${ROS_VERSION}-mavros"

echo -e "\n${BLUE}Scripts créés:${NC}"
echo "  - ~/start_ardusub_sitl.sh    : Démarrer ArduSub SITL"
echo "  - ~/connect_mavproxy.sh      : Connecter MAVProxy"

echo -e "\n${BLUE}Pour démarrer ArduSub SITL:${NC}"
echo "  ~/start_ardusub_sitl.sh"

echo -e "\n${BLUE}Pour démarrer avec Gazebo:${NC}"
echo "  ~/start_ardusub_sitl.sh --gazebo"

echo -e "\n${BLUE}Pour lancer MAVROS:${NC}"
echo "  ros2 launch mavros apm.launch fcu_url:=udp://:14540@:14557"

echo -e "\n${YELLOW}Redémarrez votre terminal pour appliquer les changements.${NC}"
