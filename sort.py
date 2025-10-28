# ---------- 仙人掌排序 ----------

# 单向冒泡排序
# 待优化：双向冒泡排序

# 列排序
def sort_col():
	n = get_world_size()
	for i in range(n):
		swapped = False
		for j in range(n):
			if measure() < measure(South) and get_pos_y() != 0:
				swap(South)
				swapped = True
			move(South)
		if not swapped:
			break
		
# 行排序
def sort_row():
	n = get_world_size()
	for i in range(n):
		swapped = False
		for j in range(n):
			if measure() > measure(East) and get_pos_x() != n - 1:
				swap(East)
				swapped = True
			move(East)	
		if not swapped:
			break