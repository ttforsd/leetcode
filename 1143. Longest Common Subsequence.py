def solver(text1, text2):
    if len(text1) > len(text2): 
        long = text1
        short = text2 
    else: 
        long = text2 
        short = text1 
    chars = set(short) 
    text1 = ""
    for c in long: 
        if c not in chars: 
            continue 
        text1 += c 
    long = text1 
    dp = [[0 for _ in short] for _ in long]
    # i corispond to long
    for i in range(len(dp)): 
        for j in range(len(dp[0])): 
            if i == 0 and j == 0: 
                if long[i] == short[j]: 
                    dp[i][j] = 1 
                continue 
            if i == 0: 
                if long[i] == short[j]: 
                    dp[i][j] = 1 
                else: 
                    dp[i][j] = dp[i][j-1]
                continue 
            if j == 0: 
                if long[i] == short[j]: 
                    dp[i][j] = 1 
                else: 
                    dp[i][j] = dp[i -1][j]
                continue 
            if long[i] == short[j]: 
                dp[i][j] = dp[i-1][j-1] + 1 
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    if len(dp) == 0: 
        return 0
    return dp[-1][-1]




text1 = "z"
text2 = "acedeergfsdfsdafge" 
print(solver(text1, text2))