# made by Louka D.

from random import randint

def add_player():
	global player_x, player_y

	player_x = round(grid_size / 2)
	player_y = round(grid_size / 2)
	grid[player_y][player_x] = player

def generate_map():
	global box_x, box_y
	box_x, box_y = 0, 0
	hole_x, hole_y = 0, 0

	while grid[box_y][box_x] != floor and grid[hole_y][hole_x] != floor:
		box_x = randint(2, grid_size - 3)
		box_y = randint(2, grid_size - 3)

		hole_x = randint(2, grid_size - 3)
		hole_y = randint(2, grid_size - 3)

	grid[box_y][box_x] = box
	grid[hole_y][hole_x] = hole

def move_player(user_input, player_position):
	global player_x, player_y

	if user_input in ['w', 's'] and grid[player_y + player_position][player_x] not in solid_objects:
		if grid[player_y + player_position][player_x] == box:
			if grid[box_y + player_position][box_x] != wall:
				move_box(user_input, player_position)
			else:
				return

		grid[player_y][player_x] = floor
		player_y += player_position
		grid[player_y][player_x] = player

	elif user_input in ['a', 'd'] and grid[player_y][player_x + player_position] not in solid_objects:
		if grid[player_y][player_x + player_position] == box:
			if grid[box_y][box_x + player_position] != wall:
				move_box(user_input, player_position)
			else:
				return

		grid[player_y][player_x] = floor
		player_x += player_position
		grid[player_y][player_x] = player

def move_box(user_input, box_position):
	global box_x, box_y

	if user_input in ['w', 's']:
		grid[box_y][box_x] = floor
		box_y += box_position
		grid[box_y][box_x] = box

	elif user_input in ['a', 'd']:
		grid[box_y][box_x] = floor
		box_x += box_position
		grid[box_y][box_x] = box
	
def print_grid():
	for i in grid:
		print(' '.join(i))

wall = '■'
floor = ' '
box = '▣'
hole = '⬚'
player = '☻'
solid_objects = [wall, hole] # objects that the player cannot push / cross

grid_size = 13
grid = [
	[
		wall if a == 0 or a == grid_size - 1 or b == 0 or b == grid_size - 1
		else floor

		for a in range(grid_size)
	]
	for b in range(grid_size)
]

player_x, player_y = 0, 0
add_player()
box_x, box_y = 0, 0
generate_map()

game_on = True
while game_on == True:
	print_grid()

	user_input = input(': ')
	if user_input == 'w': # top
		move_player(user_input, -1)
	elif user_input	== 's': # down
		move_player(user_input, +1)
	elif user_input == 'a': # left
		move_player(user_input, -1)
	elif user_input == 'd': # right
		move_player(user_input, +1)
	elif user_input == 'quit': # exit the game
		game_on = False

	index = 0
	for i in grid:
		if hole in i:
			index = grid.index(i)
	if hole not in grid[index]:
		grid[box_y][box_x] = floor
		generate_map()



