# tactic: maximise time and minimise cost
# only need pay half time
from math import inf

def main(cost, time): 
    memo = {}
    def dfs(i, remain): 
        if (i,remain) in memo: 
            return memo[(i,remain)]
        if remain <= 0: 
            return 0 
        if i >= len(cost): 
            return inf 
        pay = cost[i] + dfs(i + 1, remain - 1 - time[i])
        skip = dfs(i+1, remain)
        memo[(i,remain)] = min(pay,skip)
        return memo[(i,remain)]
    return dfs(0, len(cost))

cost = [1,2,3,2]
time = [1,2,3,2]