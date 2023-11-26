import heapq

# find loop, min edge 

def make_graph(tickets): 
    graph = {} 
    for src, dst in tickets: 
        if src not in graph: 
            graph[src] = [] 
        graph[src].append(dst)
    for src in graph: 
        graph[src].sort()
    return graph 



def solver(tickets): 
    n = len(tickets)
    graph = make_graph(tickets)
    print(graph)
    tickets = []
    def dfs(src, stops): 
        tickets.append(src)
        if stops == 0 and (src not in graph or len(graph[src]) == 0): 
            return tickets 
        if src not in graph or len(graph[src]) == 0: 
            tickets.pop()
            return None 
        prev = None 
        tmp = graph[src].copy()
        for i in range(len(tmp)): 
            if i > 0: 
                graph[src].insert(i - 1, prev)
            prev = tmp[i] 
            del graph[src][i]
            if dfs(prev, stops - 1): 
                return tickets
        tickets.pop() 
        if prev: 
            graph[src].append(prev)
    return dfs("JFK", n)



tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]

print(solver(tickets))