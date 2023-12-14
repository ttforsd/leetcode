from collections import defaultdict

def make_graph(edges): 
    graph = defaultdict(list)
    for winner, loser in edges: 
        graph[loser].append(winner) 
    return graph 


def solver(n, edges): 
    winner = [] 
    graph = make_graph(edges) 
    visited = set() 

    def dfs(node): 
        if node in visited: 
            return 
        visited.add(node)
        if node not in graph: 
            winner.append(node)
            return 
        for nei in graph[node]: 
            dfs(nei)
    for i in range(n): 
        if i not in visited: 
            dfs(i)
    if len(winner) != 1: 
        return -1 
    return winner[0]


n = 4
edges = [[0,2],[1,3],[1,2]]

print(solver(n, edges))