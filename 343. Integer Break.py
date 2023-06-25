def solver(n): 
    dp = [1 for i in range(n)]
    for i in range(n): 
        for j in range(i): 
            dp[i] = max(dp[i], (i - j) * dp[j], (j+1) * (i - j))
    return dp