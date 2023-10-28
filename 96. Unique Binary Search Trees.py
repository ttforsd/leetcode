def solver(n): 
    return dfs(n + 1) 


def dfs(n, memo = {}): 
    if n in memo: 
        return memo[n] 
    if n == 1: 
        return 1 
    count = 0
    for i in range(1, n): 
        comb = dfs(i) * dfs(n-i) 
        count += comb 
    memo[n] = count 
    return count 