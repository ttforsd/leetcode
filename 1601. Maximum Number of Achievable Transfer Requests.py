# find all the cycles, store element and length 
# find max sum len of cycles, no repeated element use 

def solver(n, requests): 
    graph = l2graph(requests)
    cycles =  dfs(graph)
    merge = [[]]
    longest = 0 
    for cycle in cycles: 
        if len(cycle) == len(graph): 
            return len(graph)
        l = len(merge)
        for i in range(l): 
            if distinct(merge[i], cycle): 
                longest = max(longest, len(merge[i] + cycle))
                merge.append([merge[i] + cycle])
    return longest




def dfs(graph): 
    visited = set()
    cycles = [] 
    stack = []
    # current node, visited nodes (in order, so list), set of visited nodes, length
    for node in graph: 
        if node not in visited: 
            stack.append([node, [node], set([node]), 1])
        while len(stack) != 0: 
            current = stack.pop()
            current_node = current[0]
            for next in graph[current_node]: 
                l_visited = current[1].copy()
                print(l_visited)
                s_visited = current[2].copy()
                l = current[3]
                visited.add(current_node)
                if next in s_visited: 
                    index = l_visited.index(next)
                    print(next, l_visited)
                    cycles.append(l_visited[index:])
                else: 
                    l_visited.append(next)
                    s_visited.add(next)
                    l += 1 
                    stack.append([next, l_visited.copy(), s_visited.copy(), l])
    return cycles



def l2graph(requests): 
    graph = {} 
    for i in range(len(requests)): 
        if i not in graph: 
            graph[i] = [] 
        for j in range(len(requests)):
            if requests[i][1] == requests[j][0]: 
                graph[i].append(j)
    return graph

def max_swaps(cycles):
    if len(cycles) == 1: 
        return len(cycles[0])
    

def distinct(a, b): 
    for _ in a: 
        if _ in b: 
            return False 
    return True


a = [[1,2], [1,2],[2,1]]
a = [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]