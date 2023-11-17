def solver(gas, cost): 
    diff = [gas[i] - cost[i] for i in range(len(cost))]
    if sum(diff) < 0: 
        return -1 
    tank = 0 
    distance = 0 
    l = 0 
    r = 0 
    while distance < len(gas): 
        tank += diff[r % len(gas)] 
        distance += 1
        while tank < 0: 
            tank -= diff[l% len(gas)] 
            l += 1
            distance -= 1 
            if distance == 0: 
                r = l - 1
                distance = 0
        r += 1
    return l 


gas = [1,2,3,4,5]


cost = [3,4,5,1,2]


print(solver(gas, cost))