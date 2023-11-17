def solver(n): 
    factors = [2,3,5]
    pos = [0,0,0]
    dp = [1]
    while len(dp) < n: 
        comb = [factors[i] * dp[pos[i]] for i in range(len(pos))]
        next = min(comb) 
        dp.append(next) 
        for i in range(len(comb)): 
            if next == comb[i]: 
                pos[i] += 1 
    print(dp)
    return dp[-1]

print(solver(1690))