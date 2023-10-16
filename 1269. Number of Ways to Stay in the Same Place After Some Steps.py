def main(steps, arrLen): 
    memo = {} 

    def dfs(steps, x): 
        if (steps,x) in memo: 
            return memo[steps,x]
        if x < 0 or x >= arrLen: 
            return 0 
        if steps == 0 and x == 0: 
            return 1 
        if steps == 0 and x != 0: 
            return 0 
        moves = [-1,0,1]
        poss = 0 
        for move in moves: 
            paths = dfs(steps-1, x + move)
            poss += paths
        memo[(steps,x)] = poss
        return poss
    return dfs(steps, 0) % (10**9  + 7)

def tb(steps, arrLen): 
    moves = [-1,0,1]
    # steps, position 
    n = min(steps//2 + 1, arrLen)
    dp = [[0 for i in range(n)] for i in range(steps + 1)]
    dp[0][0] = 1
    for i in range(1, len(dp)): 
        for j in range(len(dp[0])): 
            poss = 0
            for move in moves: 
                if j + move < 0 or j + move >= n: 
                    pass
                else: 
                    dp[i][j] += dp[i-1][j+move]
    return dp[-1][0] % (10 ** 9 + 7)

    

while True: 
    steps = int(input("steps"))
    l = int(input("len"))
    print(tb(steps,l))


