#!/usr/bin/python3

def not_visited(cell, visited):
    not_visited = True
    #print(visited)
    for visited_cell in visited:
        if cell[1] == visited_cell[1] and cell[2] == visited_cell[2]:
            #print(cell,visited_cell)
            not_visited = False
    return not_visited

def get_connecting_cells(cells, start, visited, grid, length):
    
    for cell in cells:
        if length != 0 and cell == start:
            return (length+1) / 2
        else:
            connecting_cells = []
            #print(length,grid)
            print("\ncurrent cell",cell)
            print(visited)
            print("current length", length)
            up = (grid[cell[2]-1][cell[1]], cell[1], cell[2]-1)
            down = (grid[cell[2]+1][cell[1]], cell[1], cell[2]+1)
            left = (grid[cell[2]][cell[1]-1], cell[1]-1, cell[2])
            right = (grid[cell[2]][cell[1]+1], cell[1]+1, cell[2])
            print(length, up, down, left, right)
            if (up[0] == 'S' or down[0] == 'S' or left[0] == 'S' or right[0] == 'S') and length > 1:
                 return (length+1)/2
            if cell[0] == 'J':
                if up[0] == 'F' or up[0] == '7' or up[0] == '|':
                    connecting_cells.append(up)
                if left[0] == 'F' or left[0] == '-' or left[0] == 'L':
                    connecting_cells.append(left)
            elif cell[0] == 'L':
                if up[0] == 'F' or up[0] == '7' or up[0] == '|':
                    connecting_cells.append(up)
                if right[0] == 'J' or right[0] == '7' or right[0] == '-':
                    connecting_cells.append(right)
            elif cell[0] == '|':
                if up[0] == 'F' or up[0] == '7' or up[0] == '|':
                    connecting_cells.append(up)
                if down[0] == 'J' or down[0] == 'L' or down[0] == '|':
                    connecting_cells.append(down)
            elif cell[0] == 'F':
                if right[0] == 'J' or right[0] == '7' or right[0] == '-':
                    connecting_cells.append(right)
                if down[0] == 'J' or down[0] == 'L' or down[0] == '|':
                    connecting_cells.append(down)
            elif cell[0] == '7':
                if down[0] == 'L' or down[0] == 'J' or down[0] == '|':
                    connecting_cells.append(down)
                if left[0] == 'F' or left[0] == '-' or left[0] == 'L':
                    connecting_cells.append(left)
            elif cell[0] == '-':
                if right[0] == 'J' or right[0] == '7' or right[0] == '-':
                    connecting_cells.append(right)
                if left[0] == 'F' or left[0] == '-' or left[0] == 'L':
                    connecting_cells.append(left)
            elif cell[0] == 'S':
                if up[0] == '7' or up[0] == 'F' or up[0] == '|':
                    connecting_cells.append(up)
                if down[0] == 'L' or down[0] == 'J' or down[0] == '|':
                    connecting_cells.append(down)
                if left[0] == 'L' or left[0] == 'F' or left[0] == '-':
                    connecting_cells.append(left)
                if right[0] == '7' or right[0] == 'J' or right[0] == '-':
                    connecting_cells.append(right)
            print("connecting cells", connecting_cells)
            #print("visited", visited)
            new_cells = []
            print(visited)
            for ncell in connecting_cells:
                if not_visited(ncell, visited):
                    new_cells.append(ncell)
            print("next cells",new_cells)
            print(cell)
            visited = visited.append(cell)
            print('v',visited)
            
            return (new_cells, visited)
            #return get_connecting_cells(new_cells, start, [cell], grid, length + 1)
		
		
def find_start(grid):
	buffer='.' * (len(grid[0])+1)
	grid.insert(0, buffer)
	grid.append(buffer)
	start = ()
	for y in range(1, len(grid)-1):
		grid[y] = '.' + grid[y].strip() + '.'
		for x in range(0, len(grid[0])):
			if grid[y][x] == 'S':
				start = ('S', x, y)
	return start

def main():
    f = open("input.txt", "r")
    grid = f.readlines()#print("start",len(grid[0]), len(grid))
    start = find_start(grid)#print(start)
    cells = get_connecting_cells([start], start, [], grid, 0)
    i=1
    while type(cells) == tuple:
        cells = get_connecting_cells(cells[0], start, cells[1], grid, i)
        i+=1
        
    print(cells)
	

if __name__ == "__main__":
    main()
