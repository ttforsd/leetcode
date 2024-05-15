from collections import defaultdict, deque

def solver(n, edges): 
    graph = make_graph(edges)
    deadends = deque()
    for node in graph: 
        if len(graph[node]) == 1: 
            deadends.append(node)

    while len(graph) > 2: 
        for i in range(len(deadends)): 
            cur = deadends.popleft() 
            for nei in graph[cur]: 
                graph[nei].remove(cur)
                if len(graph[nei]) == 1: 
                    deadends.append(nei)
            del graph[cur]
    return list(graph.keys())
        

def make_graph(edges): 
    graph = defaultdict(set) 
    for x, y in edges: 
        graph[x].add(y)
        graph[y].add(x) 
    return graph 


n = 4
edges = [[1,0],[1,2],[1,3]]

# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]


print(solver(n, edges))