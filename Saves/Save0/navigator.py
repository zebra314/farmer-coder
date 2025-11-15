start_x = 0
start_y = 0
end_x = get_world_size() - 1
end_y = get_world_size() - 1

def move2():
	x = get_pos_x()
	y = get_pos_y()

	if y % 2 == 1:
		if x == 0:
			move(North)
		else:
			move(West)

		return

	if y % 2 == 0:
		if x == end_x:
			move(North)
		else:
			move(East)

		return

def move3(target_x, target_y):
	x = get_pos_x()
	y = get_pos_y()

	dx = x - target_x
	dy = y - target_y

	if dy < 0:
		for _ in range(abs(dy)):
			move(South)
	elif dy > 0:
		for _ in range(abs(dy)):
			move(North)

	if dx < 0:
		for _ in range(abs(dx)):
			move(West)
	elif dx > 0:
		for _ in range(abs(dx)):
			move(East)
