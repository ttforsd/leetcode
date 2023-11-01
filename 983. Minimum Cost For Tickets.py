from math import inf

def solver(days, costs): 
    store = [0] * days[-1]
    dp = set(days)
    tmp = 0 
    for i in range(len(store)): 
        if i + 1 in dp: 
            tmp += 1 
        store[i] = tmp 
    dp = [inf for _ in days]
    tickets = [1, 7, 30]
    for i in range(len(dp)): 
        if i == 0: 
            dp[i] = min(costs)
        day = days[i] 
        for j, t in enumerate(tickets): 
            offset = day - t - 1
            if offset < 0: 
                dp[i] = min(dp[i], costs[j]) 
                continue
            check = store[offset] - 1 
            if check >= 0: 
                dp[i] = min(dp[i], dp[check] + costs[j])
            else: 
                dp[i] = min(dp[i], costs[j])
    print(dp)
    return dp[-1]
                
days = [1,4,6,7,8,20]
costs = [2,7,15]


days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
costs = [3,14,50]


print(solver(days, costs))