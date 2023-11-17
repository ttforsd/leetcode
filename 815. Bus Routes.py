from collections import deque
# construct graph, of distance
# (distance, node)
def solver(routes, source, target): 
    if source == target: 
        return 0 
    routes = [set(a) for a in routes]
    graph = {} 
    for i in range(len(routes)): 
        for j in range(i + 1, len(routes)): 
            if i not in graph: 
                graph[i] = [] 
            if j not in graph: 
                graph[j] = [] 
            if len(routes[i] & routes[j]) > 0: 
                graph[i].append(j)
                graph[j].append(i)
    queue = deque()
    for i , route in enumerate(routes): 
        if source in route: 
            queue.append((i, 1))
    visited = set()
    while len(queue) != 0: 
        route_no, bus = queue.popleft()
        if route_no in visited: 
            continue 
        visited.add(route_no)
        if target in routes[route_no]: 
            return bus
        for next_route in graph[route_no]: 
            queue.append((next_route, bus + 1))
    return -1 
    

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]

source = 15
target = 12

routes = [[1,2,7],[3,6,7]]

source = 1
target = 6

print(solver(routes, source, target))