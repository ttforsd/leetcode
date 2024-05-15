from collections import deque

def solver(deadends, target): 
    deadends = [int(_) for _ in deadends]
    deadends = set(deadends)
    target = int(target)
    if 0 in deadends: 
        return -1 
    
    queue = [[0, 0]]
    queue = deque(queue)

    while queue: 
        cur, moves = queue.popleft() 
        if cur in deadends: 
            continue 
        if cur == target: 
            return moves 
        deadends.add(cur)
        for i in range(4): 
            tmp = cur % 10 ** (i + 1) // 10 ** (i)
            if tmp == 0: 
                queue.append([cur + 10**i, moves + 1])
                queue.append([cur + 9 * (10 ** i), moves + 1])

            elif tmp == 9: 
                queue.append([cur - 10 ** i * 9, moves + 1])
                queue.append([cur - 10 ** i, moves + 1])
            else: 
                queue.append([cur - 10 ** i, moves + 1])
                queue.append([cur + 10 ** i , moves + 1])

    return -1 


deadends = ["0001", "0010", "0090"]

target = "0011"


print(solver(deadends, target))