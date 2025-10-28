from move import moveTo
from water import water

def plant_pumpkin():
	n = 7
	x, y = get_pos_x(), get_pos_y() 
	while True:
		# ===== 第一轮：只种植 =====
		moveTo(x, y)
		for i in range(n):
			for j in range(n):
				dir_x = [East, West][i % 2]
				if get_ground_type() != Grounds.Soil:
					till()
				if get_entity_type() == None:
					water()
					plant(Entities.Pumpkin)
				if j != n - 1:
					move(dir_x)
			move(North)
		moveTo(x, y)

		# ===== 第二轮：只检查死南瓜并补种 =====
		dead_pumpkins = []
		for i in range(n):
			for j in range(n):
				dir_x = [East, West][i % 2]
				if get_entity_type() == Entities.Dead_Pumpkin:
					water()
					plant(Entities.Pumpkin)
					dead_pumpkins.append((get_pos_x(), get_pos_y()))
				if j != n - 1:
					move(dir_x)
			move(North)
		moveTo(x, y)
		
		# 遍历坏南瓜列表，补种死南瓜
		while dead_pumpkins:
			for (nx, ny) in dead_pumpkins[:]:
				moveTo(nx, ny)
				
				if get_entity_type() == Entities.Pumpkin:
					dead_pumpkins.remove((nx, ny))
					continue
					
				water()
				plant(Entities.Pumpkin)
		
		# 收获
		if can_harvest():
			harvest()

		# 退出条件
		# if num_items(Items.Pumpkin) > 200000000:
			# break
	
#clear()

points = [(0, 0), 
		  (0, 8), (0, 16), (0 ,24), 
		  (8, 0), (16, 0), (24, 0), 
		  (8, 8), 
		  (16, 8), (24, 8), 
		  (8, 16), (8, 24),
		  (16, 16),
		  (16, 24), (24, 16),
		  (24, 24)]

while True:
	for (nx, ny) in points:
		moveTo(nx, ny)
		if not spawn_drone(plant_pumpkin):
			plant_pumpkin()
	
	# 退出条件
	# if num_items(Items.Pumpkin) > 200000000:
		# break
		