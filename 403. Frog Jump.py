def bfs(stones): 
    if stones[1] != 1: 
        return False
    stones = stones[1:]
    map = set(stones)
    visited = set()
    queue = []
    # current pos, last jump distance
    first = (1, 1)
    queue.append(first)
    while len(queue) != 0: 
        current = queue.pop(0)
        current_node, pre_jump = current
        if current in visited: 
            continue 
        if current_node == stones[-1]: 
            return True
        visited.add(current)
        for i in [-1,0,1]: 
            jump = i + pre_jump
            next_pos = jump + current_node
            if next_pos in map: 
                queue.append((next_pos, jump))
        
    return False 


def solver(stones):
    if stones[1] != 1: 
        return False
    stones = stones[1:]
    map = set(stones)
    visited = set()
    stack = []
    # current pos, last jump distance
    first = (1, 1)
    stack.append(first)
    while len(stack) != 0: 
        current = stack.pop()
        current_node, pre_jump = current
        if current in visited: 
            continue 
        if current_node == stones[-1]: 
            return True
        visited.add(current)
        for i in [-1,0,1]: 
            jump = i + pre_jump
            next_pos = jump + current_node
            if next_pos in map: 
                stack.append((next_pos, jump))
def dfs(): 
    pass



print(solver([0,1,3,6,10,13,15,18]))