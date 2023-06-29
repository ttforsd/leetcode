def solver(grid): 
    start, all_keys = findStart(grid)
    return bfs(grid, start, all_keys)

def findStart(grid): 
    keys = set()
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if grid[i][j] == "@": 
                start = (i,j) 
            if grid[i][j].isupper(): 
                keys.add(grid[i][j])
    return start, keys 


def entry(grid, keys, loc): 
    height = len(grid)
    width = len(grid[0])
    y, x = loc
    if y not in range(height): 
        return False 
    if x not in range(width): 
        return False 
    if grid[y][x] == "#": 
        return False
    if grid[y][x].isupper(): 
        if grid[y][x] not in keys: 
            return False 
    return True 


def bfs(grid, start, all_keys):
    # pos, visited nodes, collected keys, steps 
    queue = [(start, set(), set(), 0)]
    while len(queue) != 0: 
        # print("---")
        # print(queue[0])
        # print("---")
        (y,x), visited, keys, steps = queue.pop(0)
        dirs = [-1,1]
        for dir in dirs: 
            for i in range(2): 
                new_visited = visited.copy()
                collectedKeys = keys.copy()
                if i == 0: 
                    new_pos = (y + dir, x)
                else: 
                    new_pos = (y, x + dir)
                if (new_pos, len(collectedKeys)) in visited: 
                    continue 
                if entry(grid, collectedKeys, new_pos) == False: 
                    continue 
                else: 
                    cell = grid[new_pos[0]][new_pos[1]]
                    if cell.islower(): 
                        cell = cell.upper()
                        if cell not in collectedKeys: 
                            collectedKeys.add(cell)
                            if collectedKeys == all_keys: 
                                return steps + 1 
                    new_visited.add((new_pos, len(collectedKeys)))
                    queue.append((new_pos, new_visited.copy(), collectedKeys.copy(), steps +1))
    return -1 


grid = ["b....................@a..AB.cC"]
grid = ["..#....##.","....d.#.D#","#...#.c...","..##.#..a.","...#....##","#....b....",".#..#.....","..........",".#..##..A.",".B..C.#..@"]
for _ in grid: 
    print(_)

print(solver(grid))
print(len(grid[0]))

                

