import heapq

def makeGraph(roads): 
    graph = {} 
    for src, dst, dis in roads: 
        if src not in graph: 
            graph[src] = [] 
        if dst not in graph: 
            graph[dst] = [] 
        graph[src].append((dis, dst))
        graph[dst].append((dis, src))
    return graph 

def reachable(maxDis, blocked, all, graph): 
    if len(all) == len(blocked): 
        return True
    queue = []
    visited = set() 
    remain = all - blocked 
    heapq.heappush(queue, (0, next(iter(remain))))
    while len(queue) != 0: 
        dis, cur = heapq.heappop(queue)
        if cur in visited: 
            continue 
        visited.add(cur)
        if len(visited) == len(remain): 
            return True 
        for di, nei in graph[cur]: 
            if di + dis <= maxDis and nei not in blocked: 
                heapq.heappush(queue, (di + dis, nei))
    return False 




def solver(n, maxDistance, roads): 
    graph = makeGraph(roads)
    all = set([i for i in range(n)])
    res = 0 
    combs = [] 
    def gencomb(i, res): 
        if i == n: 
            combs.append(res.copy())
            return 
        gencomb(i+1, res)
        res.add(i) 
        gencomb(i + 1, res) 
        res.remove(i) 
    gencomb(0, set())
    for comb in combs: 
        if reachable(maxDistance, comb, all, graph): 
            res += 1 
    return res




n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]


n = 3
maxDistance = 5
roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]

maxDistance = 19
roads = [[1,0,7],[0,2,18]]


print(solver(n, maxDistance, roads))