def search_treasure():
	directions = [North, East, South, West]
	idx = 0
	
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
			
		rightIdx = (idx + 1) % 4
		behindIdx = (idx + 2) % 4
		leftIdx = (idx + 3) % 4
		
		# 右，前，左，后
		if can_move(directions[rightIdx]):
			idx = rightIdx
			move(directions[idx])
			continue
		elif can_move(directions[idx]):
			move(directions[idx])
			continue
		elif can_move(directions[leftIdx]):
			idx = leftIdx
			move(directions[idx])
			continue
		elif can_move(directions[behindIdx]):
			idx = behindIdx
			move(directions[idx])
			continue
			
		
n = get_world_size()	
			
while True:
	plant(Entities.Bush)
	substance = n * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	search_treasure()