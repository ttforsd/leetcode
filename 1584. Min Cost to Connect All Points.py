from math import inf 

def solver(points): 
    distance = 0 
    graph = make_graph(points)
    points = set([i for i in range(len(points))])
    visited = set()
    explore_graph = graph[0].copy()
    visited.add(0)
    while len(visited) != len(points): 
        d = inf
        point = None 
        for nei in explore_graph: 
            if explore_graph[nei] < d: 
                d = explore_graph[nei]
                point = nei 
        distance += explore_graph[point]
        visited.add(point)
        tmp = {} 
        for remain in points - visited: 
            tmp[remain] = min(explore_graph[remain], graph[point][remain])
        explore_graph = tmp.copy()
    return distance

        




def make_graph(points): 
    graph = {}
    for i in range(len(points)): 
        for j in range(i + 1, len(points)): 
            if i not in graph: 
                graph[i] = {} 
            if j not in graph: 
                graph[j] = {}
            graph[i][j] = abs(points[i][0] - points[j][0]) + abs(abs(points[i][-1] - points[j][-1]))
            graph[j][i] = abs(points[i][0] - points[j][0]) + abs(abs(points[i][-1] - points[j][-1]))
    return graph


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

print(solver(points))