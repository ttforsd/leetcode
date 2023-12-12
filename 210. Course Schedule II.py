import heapq
from collections import deque 

def make_graph(pre): 
    graph = {} 
    for after, before in pre: 
        if before not in graph: 
            graph[before] = [] 
        if after not in graph:
            graph[after] = [] 
        graph[before].append(after)
    return graph 


def solver(n, pre): 
    graph = make_graph(pre)
    visited = set() 
    res = [] 

    def dfs(node, path): 
        if node in path: 
            return False
        if node in visited: 
            return 
        visited.add(node)
        path.add(node)
        if node not in graph: 
            res.append(node)
            return 
        for nei in graph[node]: 
            if dfs(nei, path) == False: 
                return False 
        path.remove(node)
        res.append(node) 
    for i in range(n): 
        if i not in visited: 
            if dfs(i, set()) == False: 
                return []
    res.reverse() 
    return res



n = 4

pre = [[1,0],[2,0],[3,1],[2,3]]
pre = [[0,1],[1,0]]
print(solver(2, pre))