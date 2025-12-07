#!/bin/bash
# ==============================================================================
# Script pour désactiver protobuf 25.0 de /usr/local
# et utiliser la version système (3.12.4) compatible avec Gazebo Harmonic
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}=== Correction incompatibilité Protobuf ===${NC}"
echo ""

# Vérifier version actuelle
echo "Version protoc actuelle:"
which protoc 2>/dev/null || echo "/usr/bin/protoc"
protoc --version 2>/dev/null || /usr/bin/protoc --version
echo ""

# Vérifier si /usr/local/include/google existe
if [ -d "/usr/local/include/google" ]; then
    echo -e "${YELLOW}Désactivation des headers protobuf dans /usr/local/include...${NC}"
    sudo mv /usr/local/include/google /usr/local/include/google.protobuf25.bak
    echo -e "${GREEN}✓ Headers déplacés vers /usr/local/include/google.protobuf25.bak${NC}"
else
    echo -e "${GREEN}✓ Pas de headers protobuf dans /usr/local/include${NC}"
fi

# Vérifier si protoc existe dans /usr/local/bin
if ls /usr/local/bin/protoc* 1> /dev/null 2>&1; then
    echo -e "${YELLOW}Désactivation de protoc dans /usr/local/bin...${NC}"
    for f in /usr/local/bin/protoc*; do
        if [ -L "$f" ]; then
            sudo rm "$f"
            echo -e "${GREEN}✓ Lien symbolique $f supprimé${NC}"
        elif [ -f "$f" ]; then
            sudo mv "$f" "${f}.bak"
            echo -e "${GREEN}✓ $f renommé${NC}"
        fi
    done
fi

# Supprimer libs protobuf si présentes
if ls /usr/local/lib/libprotobuf* 1> /dev/null 2>&1 || ls /usr/local/lib/libprotoc* 1> /dev/null 2>&1; then
    echo -e "${YELLOW}Déplacement des libs protobuf...${NC}"
    sudo mkdir -p /usr/local/lib/protobuf25.bak
    sudo mv /usr/local/lib/libprotobuf* /usr/local/lib/protobuf25.bak/ 2>/dev/null || true
    sudo mv /usr/local/lib/libprotoc* /usr/local/lib/protobuf25.bak/ 2>/dev/null || true
    echo -e "${GREEN}✓ Libs déplacées${NC}"
fi

# Supprimer fichiers cmake protobuf si présents
if [ -d "/usr/local/lib/cmake/protobuf" ]; then
    echo -e "${YELLOW}Déplacement des fichiers cmake protobuf...${NC}"
    sudo mv /usr/local/lib/cmake/protobuf /usr/local/lib/cmake/protobuf.bak
    echo -e "${GREEN}✓ Fichiers cmake déplacés${NC}"
fi

echo ""
echo -e "${GREEN}=== Vérification ===${NC}"
echo "Nouvelle version protoc:"
which protoc
/usr/bin/protoc --version

echo ""
echo -e "${GREEN}=== Terminé ===${NC}"
echo "Tu peux maintenant recompiler ardupilot_gazebo:"
echo ""
echo "  cd ~/ardupilot_gazebo/build"
echo "  rm -rf *"
echo "  cmake .. -DCMAKE_BUILD_TYPE=Release"
echo "  make -j4"
echo "  sudo make install"
echo ""
echo -e "${YELLOW}Pour restaurer protobuf 25.0 plus tard:${NC}"
echo "  sudo mv /usr/local/include/google.protobuf25.bak /usr/local/include/google"
echo "  sudo mv /usr/local/bin/protoc-25.0.0.bak /usr/local/bin/protoc-25.0.0"
echo "  sudo ln -s /usr/local/bin/protoc-25.0.0 /usr/local/bin/protoc"
echo "  sudo mv /usr/local/lib/protobuf25.bak/* /usr/local/lib/"
echo "  sudo mv /usr/local/lib/cmake/protobuf.bak /usr/local/lib/cmake/protobuf"
