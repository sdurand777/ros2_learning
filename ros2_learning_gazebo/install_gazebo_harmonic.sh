#!/bin/bash
# ==============================================================================
# Script d'installation de Gazebo Harmonic (GZ Harmonic) avec ROS2 Humble/Jazzy
# ==============================================================================
#
# Ce script installe:
# - Gazebo Harmonic (gz-harmonic)
# - ros_gz bridge packages pour ROS2
# - Dépendances nécessaires
#
# Usage: ./install_gazebo_harmonic.sh
# ==============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     Installation de Gazebo Harmonic avec ROS2                ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo -e "${RED}Ne pas exécuter ce script en tant que root. Utiliser un utilisateur normal.${NC}"
    exit 1
fi

# Detect ROS2 distribution
if [ -n "$ROS_DISTRO" ]; then
    ROS_VERSION=$ROS_DISTRO
    echo -e "${GREEN}ROS2 distribution détectée: $ROS_VERSION${NC}"
else
    echo -e "${YELLOW}ROS_DISTRO non défini. Essayez de sourcer ROS2 d'abord.${NC}"
    echo -e "${YELLOW}Utilisation de 'humble' par défaut...${NC}"
    ROS_VERSION="humble"
fi

# ==============================================================================
# Step 1: Install prerequisites
# ==============================================================================
echo -e "\n${BLUE}[1/5] Installation des prérequis...${NC}"

sudo apt-get update
sudo apt-get install -y \
    curl \
    gnupg \
    lsb-release \
    wget \
    software-properties-common

# ==============================================================================
# Step 2: Add Gazebo package repository
# ==============================================================================
echo -e "\n${BLUE}[2/5] Ajout du dépôt Gazebo...${NC}"

# Add OSRF apt repository
sudo curl -sSL https://packages.osrfoundation.org/gazebo.gpg \
    -o /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] \
http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update

# ==============================================================================
# Step 3: Install Gazebo Harmonic
# ==============================================================================
echo -e "\n${BLUE}[3/5] Installation de Gazebo Harmonic...${NC}"

sudo apt-get install -y gz-harmonic

# Verify installation
echo -e "${GREEN}Vérification de l'installation Gazebo...${NC}"
gz sim --version || echo -e "${YELLOW}Note: 'gz sim --version' peut échouer sans display${NC}"

# ==============================================================================
# Step 4: Install ROS-Gazebo bridge packages
# ==============================================================================
echo -e "\n${BLUE}[4/5] Installation des packages ros_gz...${NC}"

# Install ros_gz packages for the detected ROS version
sudo apt-get install -y \
    ros-${ROS_VERSION}-ros-gz \
    ros-${ROS_VERSION}-ros-gz-bridge \
    ros-${ROS_VERSION}-ros-gz-sim \
    ros-${ROS_VERSION}-ros-gz-image \
    ros-${ROS_VERSION}-ros-gz-interfaces

# Additional useful packages
sudo apt-get install -y \
    ros-${ROS_VERSION}-xacro \
    ros-${ROS_VERSION}-robot-state-publisher \
    ros-${ROS_VERSION}-joint-state-publisher \
    ros-${ROS_VERSION}-tf2-ros \
    ros-${ROS_VERSION}-tf2-tools

# ==============================================================================
# Step 5: Setup environment
# ==============================================================================
echo -e "\n${BLUE}[5/5] Configuration de l'environnement...${NC}"

# Add Gazebo environment setup to bashrc if not already present
GAZEBO_SETUP='source /usr/share/gz/gz-harmonic/setup.bash'
if ! grep -q "gz-harmonic/setup.bash" ~/.bashrc; then
    echo "" >> ~/.bashrc
    echo "# Gazebo Harmonic environment" >> ~/.bashrc
    echo "if [ -f /usr/share/gz/gz-harmonic/setup.bash ]; then" >> ~/.bashrc
    echo "    $GAZEBO_SETUP" >> ~/.bashrc
    echo "fi" >> ~/.bashrc
    echo -e "${GREEN}Ajouté setup Gazebo à ~/.bashrc${NC}"
fi

# Set GZ_VERSION environment variable
if ! grep -q "GZ_VERSION" ~/.bashrc; then
    echo "export GZ_VERSION=harmonic" >> ~/.bashrc
    echo -e "${GREEN}Ajouté GZ_VERSION=harmonic à ~/.bashrc${NC}"
fi

# Source the setup
if [ -f /usr/share/gz/gz-harmonic/setup.bash ]; then
    source /usr/share/gz/gz-harmonic/setup.bash
fi

# ==============================================================================
# Summary
# ==============================================================================
echo -e "\n${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║               Installation terminée avec succès!              ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"

echo -e "\n${BLUE}Packages installés:${NC}"
echo "  - Gazebo Harmonic (gz-harmonic)"
echo "  - ros-${ROS_VERSION}-ros-gz"
echo "  - ros-${ROS_VERSION}-ros-gz-bridge"
echo "  - ros-${ROS_VERSION}-ros-gz-sim"
echo "  - ros-${ROS_VERSION}-ros-gz-image"

echo -e "\n${BLUE}Pour utiliser Gazebo Harmonic:${NC}"
echo "  1. Redémarrer le terminal ou exécuter: source ~/.bashrc"
echo "  2. Lancer Gazebo: gz sim"
echo "  3. Lancer un monde: gz sim -r <world.sdf>"

echo -e "\n${BLUE}Pour tester ros_gz_bridge:${NC}"
echo "  ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist"

echo -e "\n${BLUE}Documentation:${NC}"
echo "  - Gazebo: https://gazebosim.org/docs/harmonic"
echo "  - ros_gz: https://github.com/gazebosim/ros_gz"

echo -e "\n${YELLOW}Note: Redémarrez votre terminal pour appliquer les changements d'environnement.${NC}"
