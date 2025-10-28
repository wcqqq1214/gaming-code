def water():
	if num_items(Items.Water) < 5:
		return
	
	if get_water() < 0.75:
		use_item(Items.Water)