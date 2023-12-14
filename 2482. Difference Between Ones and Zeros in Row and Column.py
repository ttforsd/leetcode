def solver(grid): 
    nr = len(grid)
    nc = len(grid[0])
    rows = [0 for _ in grid] 
    cols = [0 for _ in grid[0]]
    for i in range(nr): 
        for j in range(nc): 
            rows[i] += grid[i][j] 
            cols[j] += grid[i][j] 
    for i in range(nr): 
        for j in range(nc): 
            grid[i][j] = rows[i] + cols[j] - (nr - rows[i]) - (nc - cols[j])
    return grid 


grid = [[0,1,1],[1,0,1],[0,0,1]]


print(solver(grid))