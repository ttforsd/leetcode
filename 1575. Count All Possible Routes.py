def list2graph(locs): 
    graph = dict()
    for i in range(len(locs)  - 1): 
        for j in range(len(locs) - i - 1): 
            k = i + j + 1
            if i not in graph: 
                graph[i] = [] 
                graph[i].append((k, abs(locs[i] - locs[k])))
            else: 
                graph[i].append((k, abs(locs[i] - locs[k])))
            if k not in graph: 
                graph[k] = [] 
                graph[k].append((i, abs(locs[i] - locs[k])))
            else: 
                graph[k].append((i, abs(locs[i] - locs[k])))
    return graph 
        
def main(locs, start, finish, fuel): 
    graph = list2graph(locs)
    return solver(graph, start, finish, fuel) % (10**9 + 7)

def solver(graph, start, finish, fuel, cache={}):
    if fuel == 0 and start == finish: 
        return 1
    if fuel < 0: 
        return 0 
    if fuel == 0 and start != finish: 
        return 0 
    if (start, fuel) in cache: 
        return cache[(start,fuel)]
    ways = 0 
    arrived = 0 
    if start == finish: 
        arrived = 1
    for a, b in graph[start]: 
        ways += solver(graph, a, finish, fuel - b, cache)
    ways += arrived
    cache[(start,fuel)] = ways
    return ways