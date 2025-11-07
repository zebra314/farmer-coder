# Farmer Coder

Code [The Farmer was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) Steam game in external editor on Linux.

## Setup with script

Simply run:

```sh
./setup.sh
```

[The script](./setup.sh) automatically:

- Finds the game’s Steam AppID
- Moves your Saves folder to the current folder
- Creates a symbolic link back to the game folder

## Setup manually

1. Find the Steam AppID

```sh
grep -i "The Farmer Was Replaced" ~/.local/share/Steam/steamapps/*.acf
```

It should output something like:

```sh
/home/you/.local/share/Steam/steamapps/appmanifest_1234560.acf
```

That number (e.g. `1234560`) is the AppID.

2. Move the data files to your development folder

Assume your development folder is `~/farmer-code/` and your AppID is `2060160`, run:

```sh
mv "$HOME/.local/share/Steam/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/Saves" ~/farmer-code/
```

3. Create the symbolic link back to the game folder

```sh
ln -s ~/farmer-code/Saves "$HOME/.local/share/Steam/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/Saves"
```

- Verify

Check that the symbolic link was created correctly:

```sh
ls -l "$HOME/.local/share/Steam/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/"
```

You should see:

```sh
Saves -> /home/you/farmer-code/Saves
```

Now the game reads and writes your code directly inside your Git repo.
