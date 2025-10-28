def moveTo(x, y):
	dx, dy = x - get_pos_x(), y - get_pos_y()

	if abs(dx) > get_world_size() // 2:
		dx *= -1
	if abs(dy) > get_world_size() // 2:
		dy *= -1

	dir_x = [West, East][dx > 0]
	dir_y = [South, North][dy > 0]

	while get_pos_x() != x:
		move(dir_x)

	while get_pos_y() != y:
		move(dir_y)