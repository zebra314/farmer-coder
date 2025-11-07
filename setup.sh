#!/bin/bash
# Script to move The Farmer Was Replaced Saves folder to a development folder
# and create a symlink so the game uses it.

set -e  # Exit on error

# Find AppID
APPID=$(grep -i "The Farmer Was Replaced" ~/.local/share/Steam/steamapps/*.acf | head -n1 | sed -E 's/.*appmanifest_([0-9]+)\.acf.*/\1/')
if [ -z "$APPID" ]; then
    echo "Error: Could not find AppID for The Farmer Was Replaced in Steam library."
    exit 1
fi
echo "Detected AppID: $APPID"

# Define paths
SAVES_SRC="$HOME/.local/share/Steam/steamapps/compatdata/$APPID/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/Saves"
DEV_FOLDER="$(pwd)"
SAVES_DEST="$DEV_FOLDER/Saves"

# Check if the source exists
if [ -L "$SAVES_SRC" ]; then
    # Already a symlink, do nothing
    echo "Saves folder is already a symbolic link."
elif [ "$SAVES_SRC" -ef "$SAVES_DEST" ]; then
    # Source and destination are the same folder (already moved)
    echo "Saves folder is already in the development folder."
elif [ -d "$SAVES_SRC" ]; then
    # Normal case: move the folder
    echo "Moving Saves folder to development folder..."
    mv "$SAVES_SRC" "$SAVES_DEST"
else
    echo "Error: Saves folder not found at $SAVES_SRC"
    exit 1
fi

# Create symbolic link back to game folder
if [ ! -L "$SAVES_SRC" ]; then
    echo "Creating symbolic link back to game folder..."
    ln -s "$SAVES_DEST" "$SAVES_SRC"
else
    echo "Symbolic link already exists."
fi

# Verify
echo "Symbolic link created at game folder:"
ls -l "$SAVES_SRC"

echo "Done! You can now edit scripts in $SAVES_DEST"