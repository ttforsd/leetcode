# loop is not possible given the constraint, thus not need consider visited

def solver(matrix, memo = {}): 
    def dfs(pos): 
        if pos in memo: 
            return memo[pos]
        x, y = pos
        value = matrix[x][y]
        moves = [-1,1]
        pos_nei = [] 
        for move in moves: 
            x_move = x + move 
            y_move = y + move 
            if 0 <= x_move < len(matrix) and matrix[x_move][y] > value: 
                pos_nei.append((x_move, y))
            if 0 <= y_move < len(matrix[0]) and matrix[x][y_move] > value: 
                pos_nei.append((x, y_move))
        if len(pos_nei) == 0: 
            memo[pos] = 1 
            return 1 
        tmp = 0
        for nei in pos_nei: 
            tmp = max(tmp, dfs(nei))
        memo[pos] = 1 + tmp 
        return 1 + tmp
    ans = 0 
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])): 
            ans = max(ans, dfs((i,j)))
    return ans


matrix = [[9,9,4],[6,6,8],[2,1,1]]


print(solver(matrix))