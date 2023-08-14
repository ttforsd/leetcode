def solver(s, t): 
    dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
    dp[0] = [1 for i in range(len(s) + 1)]
    print(dp)
    for i in range(1, len(dp)): 
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i][j-1]
            if s[j-1] == t[i-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[-1]


s = "aabab"
t = "ab"

s = "rabbbit"
t = "rabbit"