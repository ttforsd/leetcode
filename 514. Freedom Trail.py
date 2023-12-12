from collections import defaultdict
from math import inf 

def make_graph(ring): 
    graph = defaultdict(list) 
    for i, c in enumerate(ring): 
        graph[c].append(i)
    return graph 

def solver(ring, key): 
    l = len(ring) 
    ring  = make_graph(ring)
    memo = {} 
    def helper(src, dst): 
        diff = abs(src - dst) 
        return min(l - diff, diff)
    def recur(i, pos): 
        if i == len(key): 
            return 0 
        if (i, pos) in memo: 
            return memo[(i, pos)] 
        res = inf 
        for new_pos in ring[key[i]]: 
            res = min(res, helper(new_pos, pos) + 1 + recur(i + 1, new_pos))
        memo[(i, pos)] = res 
        return res 
    return recur(0, 0)




ring = "godding"
key = "gd"

ring = "godding"
key = "godding"
print(solver(ring, key))
