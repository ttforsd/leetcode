# if 0, must be end 

def solver(s): 
    dp = [0 for i in range(len(s))]
    if s[0] == '0': 
        return 0
    if len(s) == 1: 
        return 1
    holder = int(s[:2])
    dp[0] = 1 
    if holder % 10 != 0 and holder <= 26: 
        dp[1] = 2
    elif holder % 10 == 0 and holder > 20: 
        return 0
    else: 
        dp[1] = 1
    for i in range(2, len(dp)): 
        holder = int(s[i])
        if holder != 0: 
            dp[i] += dp[i - 1]
        holder = int(s[i-1:i+1])
        if 10 <= holder <= 26: 
            dp[i] += dp[i - 2]
        if dp[i] == 0: 
            return 0
    return dp[-1]

s = "12"
print(solver(s))

