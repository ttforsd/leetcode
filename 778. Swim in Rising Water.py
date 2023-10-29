import heapq

def solver(grid): 
    time = 0 
    # datastructure in heap (height, x, y)
    rows, cols = len(grid), len(grid[0])
    heap = []
    heapq.heappush(heap, (0,0,0))
    visited = set()
    while len(heap) != 0: 
        height, x, y= heapq.heappop(heap)
        if (x,y) in visited: 
            continue 
        visited.add((x,y))
        time = max(time, height)
        if x == rows - 1 and y == cols - 1: 
            break 
        if x - 1 >= 0: 
            heapq.heappush(heap, (grid[x-1][y], x-1, y))
        if x + 1 < rows: 
            heapq.heappush(heap, (grid[x + 1][y], x + 1, y))
        if y - 1 >= 0: 
            heapq.heappush(heap, (grid[x][y - 1], x, y - 1))
        if y + 1 < cols: 
            heapq.heappush(heap, (grid[x][y + 1], x, y + 1))
    return time


grid = [[0,2],[1,3]]
print(solver(grid))