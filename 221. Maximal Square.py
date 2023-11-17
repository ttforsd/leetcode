def solver(matrix): 
    res = 0 
    dp = [[(0,0,0) for _ in matrix[0]] for _ in matrix]
    # height, width, max sq 
    for i in range(len(dp)): 
        for j in range(len(dp[0])): 
            if matrix[i][j] == "0": 
                continue 
            if i == 0 and j == 0: 
                dp[i][j] = (1,1,1)
                res = max(1, res)
                continue 
            if j == 0: 
                w = 1 
                h = 1 + dp[i-1][j][0]
                dp[i][j] = (h, w, 1)
                res = max(1, res)
                continue
            if i == 0: 
                h = 1 
                w = 1 + dp[i][j - 1][1]
                dp[i][j] = (h, w, 1)
                res = max(1, res)
                continue 
            h = dp[i-1][j][0] + 1 
            w = dp[i][j-1][1] + 1 
            sq = min(dp[i-1][j][0], dp[i][j-1][1], dp[i-1][j-1][-1]) + 1 
            res = max(sq, res)
            dp[i][j] = (h, w, sq)
    return res ** 2
                
m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
m = [["0","1"],["1","0"]]
m = [["1"]]
for _ in m: 
    print(_)


print(solver(m))