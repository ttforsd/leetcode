def make_graph(heights): 
    moves = [-1, 1]
    graph = {}
    for i in range(len(heights)): 
        for j in range(len(heights[0])): 
            graph[(i,j)] = []
            for move in moves: 
                x_move = i + move 
                y_move = j + move 
                if 0 <= x_move < len(heights) and heights[i][j] >= heights[x_move][j]: 
                    graph[(i,j)].append((x_move, j))
                if 0 <= y_move < len(heights[0]) and heights[i][j] >= heights[i][y_move]: 
                    graph[(i,j)].append((i, y_move))
    return graph 

                

def solver(heights): 
    # memo that stores flow 
    memo = {}
    graph = make_graph(heights)
    # if queue empty, return result
    # if take ans from border then or all results 
    def dfs(index, path): 
        if index in memo: 
            return memo[index]
        x, y = index
        pacific, atlantic = False, False
        path.add(index)
        if x * y == 0: 
            pacific = True 
        if x == len(heights) - 1 or y == len(heights[0]) - 1: 
            atlantic = True 
        if atlantic and pacific: 
            memo[index] = (True, True)
            return (True, True)
        for nei in graph[index]: 
            if nei in path: 
                continue
            tmp0, tmp1 = dfs(nei, path.copy())
            pacific = (pacific or tmp0)
            atlantic = (atlantic or tmp1)
        if pacific and atlantic: 
            memo[index] = (True, True)
            return (True, True)
        if len(path) == 1: 
            memo[index] = (pacific, atlantic)
        return (pacific, atlantic)
    res = [] 
    for i in range(len(heights)): 
        for j in range(len(heights[0])): 
            if dfs((i,j), set()) == (True, True): 
                res.append([i,j])
    return res



heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(solver(heights))


