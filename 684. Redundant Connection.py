def make_graph(edges): 
    graph = {} 
    for a, b in edges: 
        if a not in graph: 
            graph[a] = [] 
        if b not in graph: 
            graph[b] = [] 
        graph[a].append(b)
        graph[b].append(a)
    return graph 


def solver(edges): 
    graph = make_graph(edges)
    stack = [] 
    # current, previous, visited, history
    stack.append([edges[-1][-1], None, set(), []])
    while len(stack) != 0: 
        cur, pre, visited, history = stack.pop()
        if cur in visited: 
            break 
        visited.add(cur)
        history.append(cur)
        for nei in graph[cur]: 
            if pre != nei: 
                stack.append([nei, cur, visited.copy(), history.copy()])
    loc = history.index(cur)
    visited = set(history[loc:])
    while edges: 
        a, b = edges.pop()
        if a in visited and b in visited: 
            return [a,b]

edges = [[1,2],[1,3],[2,3]]

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(solver(edges))