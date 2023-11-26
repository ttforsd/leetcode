
# for max, either remove smallest speed or smallest efficiency 


def solver(n, speed, efficiency, k): 
    s_i = [(speed[i], efficiency[i], i) for i in range(n)]
    e_i = [(efficiency[i], speed[i], i) for i in range(n)]
    all = set([i for i in range(n)])
    s_i.sort() 
    e_i.sort()
    total_speed = sum(speed)
    res = 0 
    while len(all) > 1: 
        while s_i[-1][-1] not in all: 
            s_i.pop()
        while e_i[-1][-1] not in all: 
            e_i.pop() 
        if (total_speed - s_i[-1][0]) * e_i[-1][0] > (total_speed - e_i[-1][1]) * e_i[-2][0]: 
            total_speed -= s_i[-1][0]
            all.remove(s_i[-1][-1])
            s_i.pop() 
        else: 
            total_speed -= e_i[-1][1]
            all.remove(e_i[-1][-1])
            e_i.pop() 
        if len(all) <= k: 
            res = max(res, total_speed * e_i[-1][0])
    return res


        



n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2



n = 3
speed = [2,8,2]
efficiency = [2,7,1]
k = 2

n = 8 

speed = [9,9,4,6,9,7,9,8]

efficiency = [1,9,1,9,8,1,10,1]

k = 4

print(solver(n, speed, efficiency, k))