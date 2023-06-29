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

def checker(original, new): 
    for key in original: 
        if key not in new: 
            return True 
    return False 

def bfs(grid, start, all_keys): 
    # pos, collected, steps, visited dic 
    queue = [(start, set(), 0, dict())]
    while len(queue) != 0: 
        dirs = [-1, 1]
        current = queue.pop(0)
        for dir in dirs: 
            for i in range(2): 
                pos = current[0]
                keys_collected = current[1].copy()
                steps = current[2]
                visited = current[3].copy()
                if i == 0: 
                    pos = (pos[0] + dir, pos[1])
                else: 
                    pos = (pos[0], pos[1] + dir)
                if pos in visited and len(keys_collected) <= visited[pos]: 
                    continue
                elif entry(grid, keys_collected, pos) == False: 
                    continue 
                else: 
                    cell = grid[pos[0]][pos[1]]
                    if cell.islower(): 
                        cell = cell.upper()
                        if cell not in keys_collected: 
                            keys_collected.add(cell)
                            if keys_collected == all_keys: 
                                return steps + 1
                    visited[pos] = len(keys_collected)
                    queue.append((pos, keys_collected.copy(), steps + 1, visited.copy()))
    return -1

grid = ["b....................@a..AB.cC"]
# grid = ["@abcdeABCDEFf"]
# grid = ["@.a..","###.#","b.A.B"]
# grid = ["@..aA","..B#.","....b"]
# grid = ["@Aa"]
# grid = ["@...a",".###A","b.BCc"]
# grid = ["@abcdeABCDEFf"]
grid = ["..#....##.","....d.#.D#","#...#.c...","..##.#..a.","...#....##","#....b....",".#..#.....","..........",".#..##..A.",".B..C.#..@"]
for _ in grid: 
    print(_)

print(solver(grid))
print(len(grid[0]))