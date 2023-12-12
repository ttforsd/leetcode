from collections import deque 

def solver(grid): 
    res = 0
    if len(grid) == 0: 
        return -1 
    if len(grid[0]) == 0: 
        return -1 
    visited = set()
    stack = deque()
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if grid[i][j] == 1: 
                stack.append(((i,j), 0))
    if len(stack) == 0 or len(stack) == len(grid) * len(grid[0]): 
        return -1 
    while len(stack) != 0: 
        node, distance = stack.popleft() 
        if node in visited or 0 > node[0] or node[0] >= len(grid) or 0 > node[1] or node[1] >= len(grid[0]): 
            continue 
        visited.add(node)
        print(node, distance)
        res = max(distance, res)
        for move in [-1, 1]: 
            stack.append(((node[0] + move, node[1]), distance + 1))
            stack.append(((node[0], node[1] + move), distance + 1))
    return res 


grid = [[1,0,0],[0,0,0],[0,0,0]]

print(solver(grid))