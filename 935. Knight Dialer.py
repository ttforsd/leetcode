from collections import deque 
graph = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [], 
    6: [1, 7, 0],
    7: [2, 6],
    8: [3, 1],
    9: [2, 4],
    0: [6, 4]
}


def solver(n): 
    if n == 1: 
        return 10 
    cache = [1 for i in range(10)]
    for i in range(1, n): 
        new_cache = [0 for _ in range(10)] 
        for j in range(len(new_cache)): 
            for nei in graph[j]: 
                new_cache[j] += cache[nei]
        cache = new_cache
    return sum(cache) % (10**9 + 7)
    


print(solver(3131))