import os 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    grid = [[i for i in line] for line in data]


def get_accessable_cells(grid):
    accessable_cells = [] 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue
            blocker_neighbors = 0  
            for horizontal_move in [-1, 0, 1]:
                for vertical_move in [-1, 0, 1]:
                    if horizontal_move == 0 and vertical_move == 0:
                        continue 
                    if i + horizontal_move < 0 or i + horizontal_move >= len(grid) or j + vertical_move < 0 or j + vertical_move >= len(grid[i]):
                        continue 
                    if grid[i + horizontal_move][j + vertical_move] == '@':
                        blocker_neighbors += 1
            if blocker_neighbors < 4: 
                accessable_cells.append((i, j))
    return accessable_cells

def update_grid(grid):
    count = 0
    accessable_cells = get_accessable_cells(grid)
    count += len(accessable_cells)
    while len(accessable_cells) > 0: 
        for x, y in accessable_cells:
            grid[x][y] = '.'
        accessable_cells = get_accessable_cells(grid)
        count += len(accessable_cells)
    return count

if __name__ == "__main__":
    print(update_grid(grid))