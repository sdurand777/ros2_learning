# Problème de version Protobuf avec Gazebo Harmonic

## Description du problème

Gazebo Harmonic (gz-sim8, gz-msgs10) est compilé avec **protobuf 3.12.4** (version système Ubuntu 22.04).

Si une version plus récente de protobuf (ex: 25.x) est installée dans `/usr/local/`, elle entre en conflit car:
- Les headers C++ dans `/usr/local/include/google/protobuf/` prennent priorité
- Les fichiers `.pb.h` de gz-msgs sont incompatibles avec protobuf 25.x
- Erreur de compilation: `'gz::msgs::Sensor msg' has incomplete type`

## Symptômes

Lors de la compilation de `ardupilot_gazebo` ou autre plugin Gazebo:

```
error: 'gz::msgs::Sensor msg' has incomplete type
```

Ou erreurs similaires avec d'autres types `gz::msgs::*`.

## Diagnostic

### 1. Vérifier quelle version de protoc est utilisée

```bash
which protoc
protoc --version
```

**Résultat attendu (correct):**
```
/usr/bin/protoc
libprotoc 3.12.4
```

**Résultat problématique:**
```
/usr/local/bin/protoc
libprotoc 25.0
```

### 2. Vérifier si protobuf 25.x est installé dans /usr/local

```bash
ls -la /usr/local/bin/protoc*
ls -la /usr/local/include/google/protobuf/ 2>/dev/null | head -5
ls -la /usr/local/lib/cmake/protobuf/ 2>/dev/null
```

## Solution

### Option 1: Script automatique

Utiliser le script `fix_protobuf.sh`:

```bash
cd ~/ros2_learning
./fix_protobuf.sh
```

### Option 2: Commandes manuelles

```bash
# 1. Déplacer les headers protobuf 25.x
sudo mv /usr/local/include/google /usr/local/include/google.protobuf25.bak

# 2. Déplacer le binaire protoc
sudo mv /usr/local/bin/protoc-25.0.0 /usr/local/bin/protoc-25.0.0.bak
sudo rm -f /usr/local/bin/protoc  # supprimer le lien symbolique

# 3. Déplacer les libs (si présentes)
sudo mkdir -p /usr/local/lib/protobuf25.bak
sudo mv /usr/local/lib/libprotobuf* /usr/local/lib/protobuf25.bak/ 2>/dev/null || true
sudo mv /usr/local/lib/libprotoc* /usr/local/lib/protobuf25.bak/ 2>/dev/null || true

# 4. Déplacer les fichiers cmake (si présents)
sudo mv /usr/local/lib/cmake/protobuf /usr/local/lib/cmake/protobuf.bak 2>/dev/null || true

# 5. Vérifier
which protoc
protoc --version  # doit afficher 3.12.4
```

### Après la correction

Recompiler le package problématique:

```bash
cd ~/ardupilot_gazebo/build
rm -rf *
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j4
sudo make install
```

## Restaurer protobuf 25.x (si nécessaire)

Si tu as besoin de protobuf 25.x pour d'autres projets:

```bash
sudo mv /usr/local/include/google.protobuf25.bak /usr/local/include/google
sudo mv /usr/local/bin/protoc-25.0.0.bak /usr/local/bin/protoc-25.0.0
sudo ln -s /usr/local/bin/protoc-25.0.0 /usr/local/bin/protoc
sudo mv /usr/local/lib/protobuf25.bak/* /usr/local/lib/
sudo mv /usr/local/lib/cmake/protobuf.bak /usr/local/lib/cmake/protobuf
```

## Prévention

Pour éviter ce problème à l'avenir:
- Utiliser des environnements virtuels Python pour les projets nécessitant protobuf récent
- Utiliser Docker pour isoler les environnements
- Ne pas installer protobuf manuellement dans /usr/local sur un système avec Gazebo

## Versions compatibles

| Composant | Version | Protobuf |
|-----------|---------|----------|
| Ubuntu 22.04 | - | 3.12.4 |
| Gazebo Harmonic | gz-sim8, gz-msgs10 | 3.12.4 |
| ardupilot_gazebo | main | 3.12.4 |
