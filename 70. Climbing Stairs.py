def solver(n, cache={}): 
    if n == 1: 
        return 1 
    if n == 2: 
        return 2
    if n in cache: 
        return cache[n]
    ways = solver(n - 1, cache) + solver(n - 2, cache)
    cache[n] = ways
    return ways 
    

print(solver(3))