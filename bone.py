# 使用 哈密顿回路 (Hamiltonian cycle) 暴力

from move import moveTo

n = 32

set_world_size(n)

clear()
change_hat(Hats.Dinosaur_Hat)

cnt = 0

while True:
	for i in range(n - 1):
		move(East)
		
	move(North)

	for i in range(n):
		if i % 2 == 0:
			for _ in range(n - 2):
				move(North)
		else:
			for _ in range(n - 2):
				move(South)
				
		move(West)
		
	flag = move(South)
	
	if not flag:
		change_hat(Hats.Wizard_Hat)
		moveTo(0, 0)
		change_hat(Hats.Dinosaur_Hat)
	