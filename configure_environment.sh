#!/bin/bash
# ==============================================================================
# Script de configuration de l'environnement ros2_learning
# ==============================================================================
# Configure les variables d'environnement pour:
# - Gazebo Harmonic
# - ArduPilot Gazebo Plugin
# - ROS2 workspace
# ==============================================================================

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}=== Configuration environnement ros2_learning ===${NC}"

# ==============================================================================
# Gazebo Harmonic
# ==============================================================================
if ! grep -q "gz-harmonic" ~/.bashrc; then
    echo -e "${YELLOW}Ajout configuration Gazebo Harmonic...${NC}"
    cat >> ~/.bashrc << 'EOF'

# Gazebo Harmonic
if [ -f /usr/share/gz/gz-harmonic/setup.bash ]; then
    source /usr/share/gz/gz-harmonic/setup.bash
fi
export GZ_VERSION=harmonic
EOF
    echo -e "${GREEN}✓ Gazebo Harmonic configuré${NC}"
else
    echo -e "${GREEN}✓ Gazebo Harmonic déjà configuré${NC}"
fi

# ==============================================================================
# ArduPilot Gazebo Plugin
# ==============================================================================
if [ -d "$HOME/ardupilot_gazebo" ]; then
    if ! grep -q "ardupilot_gazebo" ~/.bashrc; then
        echo -e "${YELLOW}Ajout configuration ArduPilot Gazebo...${NC}"
        cat >> ~/.bashrc << 'EOF'

# ArduPilot Gazebo Plugin
export GZ_SIM_SYSTEM_PLUGIN_PATH="$HOME/ardupilot_gazebo/build:$GZ_SIM_SYSTEM_PLUGIN_PATH"
export GZ_SIM_RESOURCE_PATH="$HOME/ardupilot_gazebo/models:$HOME/ardupilot_gazebo/worlds:$GZ_SIM_RESOURCE_PATH"
EOF
        echo -e "${GREEN}✓ ArduPilot Gazebo configuré${NC}"
    else
        echo -e "${GREEN}✓ ArduPilot Gazebo déjà configuré${NC}"
    fi
else
    echo -e "${YELLOW}⚠ ardupilot_gazebo non trouvé dans ~/ardupilot_gazebo${NC}"
fi

# ==============================================================================
# ArduPilot SITL
# ==============================================================================
if [ -d "$HOME/ardupilot" ]; then
    if ! grep -q "ardupilot/Tools/autotest" ~/.bashrc; then
        echo -e "${YELLOW}Ajout configuration ArduPilot SITL...${NC}"
        cat >> ~/.bashrc << 'EOF'

# ArduPilot SITL
export PATH="$HOME/ardupilot/Tools/autotest:$PATH"
EOF
        echo -e "${GREEN}✓ ArduPilot SITL configuré${NC}"
    else
        echo -e "${GREEN}✓ ArduPilot SITL déjà configuré${NC}"
    fi
else
    echo -e "${YELLOW}⚠ ArduPilot non trouvé dans ~/ardupilot${NC}"
fi

# ==============================================================================
# ROS2 workspace
# ==============================================================================
WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! grep -q "ros2_learning/install/setup.bash" ~/.bashrc; then
    echo -e "${YELLOW}Ajout configuration ROS2 workspace...${NC}"
    cat >> ~/.bashrc << EOF

# ROS2 Learning Workspace
if [ -f $WORKSPACE_DIR/install/setup.bash ]; then
    source $WORKSPACE_DIR/install/setup.bash
fi
EOF
    echo -e "${GREEN}✓ ROS2 workspace configuré${NC}"
else
    echo -e "${GREEN}✓ ROS2 workspace déjà configuré${NC}"
fi

# ==============================================================================
# Résumé
# ==============================================================================
echo ""
echo -e "${GREEN}=== Configuration terminée ===${NC}"
echo ""
echo "Pour appliquer les changements:"
echo "  source ~/.bashrc"
echo ""
echo "Pour compiler le workspace ROS2:"
echo "  cd $WORKSPACE_DIR"
echo "  colcon build"
echo "  source install/setup.bash"
