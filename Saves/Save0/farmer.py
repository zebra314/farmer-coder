def plant_carrot():
    # Use water
    if num_items(Items.Water) > 0:
		use_item(Items.Water)

	# Lack material
	if num_items(Items.Wood) < 4:
		if plant_tree():
		    return
        else:
            plant(Entities.Grass)

	if num_items(Items.Hay) < 4:
		plant(Entities.Grass)
		return

	# Plant target
	if get_ground_type() == Grounds.Grassland:
		till()

	if get_ground_type() == Grounds.Soil:
		plant(Entities.Carrot)

    return True

def plant_tree():
    if (get_pos_y() % 2) == (get_pos_x() % 2):
        plant(Entities.Tree)

        # Use water
        if num_items(Items.Water) > 0:
            use_item(Items.Water)

        return True
    return False

def plant_pumpkin():
    if num_items(Items.Carrot) < 4:
        plant_carrot()

    # Plant target
	if get_ground_type() == Grounds.Grassland:
		till()

	if get_ground_type() == Grounds.Soil:
		plant(Entities.Pumpkin)

    return True


