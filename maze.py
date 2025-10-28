length = 5					
set_world_size(length)

def drone():
	n = 0
	trigger = []
	while True:
		n = n + 1
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, length * 2**(num_unlocked(Unlocks.Mazes) - 1))
			trigger.insert(0, n)
		if get_entity_type() == Entities.Treasure and len(trigger) > 3:
			if trigger[0] == trigger[1] + 1 and trigger[0] == trigger[2] + 2:
				harvest()
		if n > 1000000:
			n = 0
			trigger = []
		# if num_items(Items.Gold) >= 9863168:
			# break
			
for _ in range(length ** 2 - 1):
	spawn_drone(drone)
	if get_pos_x() == length - 1:
		move(North)
	move(East)
	
cnt = 0
	
while True:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, length * 2**(num_unlocked(Unlocks.Mazes) - 1))
	cnt = cnt + 1
	if cnt < 299:
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, length * 2**(num_unlocked(Unlocks.Mazes) - 1))
	else:
		if get_entity_type() == Entities.Treasure:
			harvest()
			cnt = 0
		
	# if num_items(Items.Gold) >= 9863168:
		# break