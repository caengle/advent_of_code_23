start = find_s()
curr = s
prev = None
visited = []
connecting_cells = get_connecting cells(start, visited)
while curr != start
for cell in connecting_cells:
	if cell != s:


def get_connecting_cells(cell, start, visited, map, length)
	connecting_cells = []
	if cell != start:
		up = map[cell[1]-1][cell[2]]
		down = map[cell[1]+1][cell[2]]
		left = map[cell[1]][cell[2]-1]
		right = map[cell[1]-1][cell[2]+1]
		
		if cell[0] == 'J'
			if up[0] == 'F' or up[0] == '7' or up[0] == '|':
				connecting_cells.append(up)
			if left[0] == 'F' or left[0] == '-' or left[0] == 'L':
				connecting_cells.append(left)
		elif cell[0] == 'L'
			if up[0] == 'F' or up[0] == '7' or up[0] == '|':
				connecting_cells.append(up)
			if right[0] == 'J' or right[0] == '7' or right[0] == '-':
				connecting_cells.append(right)
		elif cell[0] == '|'
			if up[0] == 'F' or up[0] == '7' or up[0] == '|':
				connecting_cells.append(up)
			if down[0] == 'J' or down[0] == 'L' or down[0] == '-':
				connecting_cells.append(down)
		elif cell[0] == '-'
			if right[0] == 'F' or right[0] == '7' or right[0] == '-':
				connecting_cells.append(right)
			if left[0] == 'F' or left[0] == '-' or left[0] == 'L':
				connecting_cells.append(left)
		new_cells = []
		for ncell in connecting_cells
			if not_visited(ncell, visited):
				new_cells.append(ncell)
		visited = visited + new_cells
		for ncell in new_cells:
			get_connecting_cells(ncell, start, visited, map, length + 1)
	else:
		return length / 2
		
				
		
		

	
