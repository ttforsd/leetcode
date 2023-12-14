from collections import defaultdict


def make_graph(edges): 
    graph = defaultdict(list)
    for src, dst in edges: 
        graph[src].append(dst) 
        graph[dst].append(src)
    return graph 

def solver(edges, values): 
    edges = make_graph(edges) 
    memo = {} 
    def recur(i, healthy, prev): 
        if i != 0 and len(edges[i]) == 1:
            if healthy: 
                return values[i]
            else: 
                return 0 
        if (i, healthy) in memo: 
            return memo[(i, healthy)] 
        res = 0 
        if not healthy: 
            tmp = [values[i], 0] 
            for nei in edges[i]: 
                if nei == prev: 
                    continue
                tmp[1] += recur(nei, True, i)
                tmp[0] += recur(nei, False, i) 
            res = max(tmp)
        else:  
            res += values[i]
            for nei in edges[i]: 
                if nei == prev: 
                    continue 
                res += recur(nei, True, i)
        memo[(i, healthy)] = res 
        return res 
    return recur(0, False, None)
        
edges = [[0,1],[0,2],[0,3],[2,4],[4,5]]
values = [5,2,5,2,1,1]

edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [20,10,9,7,4,3,5]


edges = [[7,0],[3,1],[6,2],[4,3],[4,5],[4,6],[4,7]]
values = [2,16,23,17,22,21,8,6]
print(solver(edges, values))