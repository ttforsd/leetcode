import heapq

def solver(k, w, profits, capital): 
    table = [] 
    for i in range(len(profits)): 
        table.append((capital[i], profits[i]))
    table.sort(reverse=True)
    capital = [] 
    res = 0 
    while k > 0: 
        while len(table) != 0 and table[-1][0] <= w: 
            tmp = table.pop()[-1] * -1 # since python only min heap 
            heapq.heappush(capital, tmp)
        if len(capital) > 0: 
            w += heapq.heappop(capital) * -1 
            k -= 1
        else: 
            return w
    return w



k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]


print(solver(k, w, profits, capital))