import heapq

class Graph:

    def __init__(self, n: int, edges):
        self.map = {} 
        for i in range(n): 
            self.map[i] = []
        for start, end, cost in edges: 
            self.map[start].append((cost, end))

    def show_map(self): 
        print(self.map)

    def addEdge(self, edge) -> None:
        start, end, cost = edge 
        self.map[start].append((cost, end))

    def shortestPath(self, node1: int, node2: int) -> int:
        # in queue, store (total cost, node)
        visited = set() 
        queue = [] 
        heapq.heappush(queue, (0, node1))
        while len(queue) != 0: 
            cost, node = heapq.heappop(queue)
            if node in visited: 
                continue 
            visited.add(node)
            if node == node2: 
                return cost 
            for next_cost, next_node in self.map[node]: 
                heapq.heappush(queue, (next_cost + cost, next_node))
        
        return -1



obj = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
obj.show_map()