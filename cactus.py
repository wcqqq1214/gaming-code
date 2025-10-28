from sort import sort_col, sort_row
from for_all import for_all_plant

while True:
	n = get_world_size()
	
	for_all_plant(Entities.Cactus)
			
	for _ in range(n):
		if not spawn_drone(sort_row):
			sort_row()
		move(South)
		
	while num_drones() > 1:
		continue
		
	for _ in range(n):
		if not spawn_drone(sort_col):
			sort_col()	
		move(East)
	
	while num_drones() > 1:
		continue

	if can_harvest():
		harvest()
	
	# if num_items(Items.Cactus) <= 33554432:
		# break