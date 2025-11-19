import navigator
import farmer

target_wood_num = 200000
target_carrot_num = 20000
target_hay_num = 20000
target_pumpkin_num = 20000

# Init item list
item_list = []
for i in range(get_world_size()):
	item_list.append([])
	for j in range(get_world_size()):
		item_list[i].append(None)

# Init check list
is_checked = []
for i in range(get_world_size()):
	is_checked.append([])
	for j in range(get_world_size()):
		is_checked[i].append(False)

# Init move sequence list
move_sequence = []
move_sequence.append((0, 0))
for y in range(get_world_size()):
	for x in range(get_world_size()):
		# Skip the leftest column
		if x == 0:
			continue

		# Revert the direction in odd row
		if y % 2 == 1:
			x = get_world_size() - x

		move_sequence.append((x, y))

# Append the leftest column
for y in range(get_world_size()):
	# Revert the direction to from top to bottom
	y = get_world_size() - 1 - y

	# Skip the bottom
	if y == 0:
		break

	move_sequence.append((0, y))

# Define get sequence index function
def get_sequence_index(x, y):
	if x == 0 and y == 0:
		return 0

	# At the leftest column
	if x == 0 and y != 0:
		index = get_world_size() * (get_world_size() - 1) + (get_world_size() - y)

	if y % 2 == 0:
		index = get_world_size() * (y - 1)

	if y % 2 == 1:
		pass

while True:
	# Navigation
	x = get_pos_x()
	y = get_pos_y()

	if y % 2 == 1:
		if x == 0:
			move(North)
		else:
			move(West)

	elif y % 2 == 0:
		if x == get_world_size() - 1:
			move(North)
		else:
			move(East)

	# if is_checked[x][y]:
	#     continue

	# Update item list
	item_list[x][y] = get_entity_type()

	# Update checked list
	if item_list[x][y] == Entities.Pumpkin and can_harvest():
		is_checked[x][y] = True

	# Harvest
	# if farmer.harvest_pumpkin(item_list):
	#     for i in range(get_world_size()):
	#         for j in range(get_world_size()):
	#             item_list[i][j] = None

	#     for i in range(get_world_size()):
	#         for j in range(get_world_size()):
	#             is_checked[i][j] = False
	harvest()

	# Plant
	# farmer.plant_pumpkin(item_list)

	wood_num = num_items(Items.Wood)
	carrot_num = num_items(Items.Carrot)
	hay_num = num_items(Items.Hay)
	pumpkin_num = num_items(Items.Pumpkin)


	if wood_num < target_wood_num:
		if farmer.plant_tree():
			continue

	if hay_num < target_hay_num:
		plant(Entities.Grass)
		continue

	if carrot_num < target_carrot_num:
		farmer.plant_carrot()
		continue

	if pumpkin_num < target_pumpkin_num:
		farmer.plant_pumpkin()
		continue

	target_wood_num *= 2
	target_carrot_num *= 2
	target_hay_num *= 2
	target_pumpkin_num *= 2
