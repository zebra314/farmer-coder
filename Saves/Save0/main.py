import navigator
import farmer

target_wood_num = 200000
target_carrot_num = 20000
target_hay_num = 20000
target_pumpkin_num = 20000

while True:
	navigator.move2()

	if can_harvest():
		harvest()

	wood_num = num_items(Items.Wood)
	carrot_num = num_items(Items.Carrot)
	hay_num = num_items(Items.Hay)
    pumpkin_num = num_items(Items.Pumpkin)

    # if pumpkin_num < target_pumpkin_num:
    #     farmer.plant_pumpkin()

	# if wood_num < target_wood_num:
    #     if farmer.plant_tree():
	# 	    continue

	# if carrot_num < target_carrot_num:
	# 	farmer.plant_carrot()
	# 	continue

	if hay_num < target_hay_num:
		plant(Entities.Grass)
		continue

	target_wood_num *= 2
    target_carrot_num *= 2
    target_hay_num *= 2
    target_pumpkin_num *= 2
