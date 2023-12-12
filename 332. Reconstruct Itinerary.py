def make_graph(tickets): 
    graph = {} 
    for src, dst in tickets: 
        if src not in graph: 
            graph[src] = [] 
        if dst not in graph: 
            graph[dst] = [] 
        graph[src].append(dst)
    return graph 

def solver(tickets): 
    tickets.sort() 
    graph = make_graph(tickets)
    res = ["JFK"] 
    def dfs(node): 
        if len(graph[node]) == 0 and len(tickets) + 1 != len(res): 
            return False 
        if len(res) == len(tickets) + 1: 
            return True 
        tmp = graph[node].copy() 
        for i, dst in enumerate(tmp): 
            res.append(dst)
            del graph[node][i]
            if dfs(dst) == False: 
                res.pop() 
                graph[node].insert(i, dst)
            else: 
                return True
        return False 
    dfs("JFK")
    return res




tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]

print(solver(tickets))