def solver(n): 
    chars = ['a', 'e', 'i', 'o', 'u']
    dp = [[0 for char in chars] for i in range(n)]
    for i in range(len(dp)): 
        for j in range(len(dp[0])): 
            if i == 0: 
                dp[i][j] = 1 
                continue 
            if j == 0: 
                dp[i][j] = dp[i-1][1] + dp[i-1][4] + dp[i-1][2]
            if j == 1: 
                dp[i][j] = dp[i-1][0] + dp[i-1][2]
            if j == 2: 
                dp[i][j] = dp[i-1][1] + dp[i-1][3]
            if j == 3: 
                dp[i][j] = dp[i-1][2] 
            if j == 4: 
                dp[i][j] = dp[i-1][3] + dp[i-1][2]
    return sum(dp[-1])


print(solver(2))