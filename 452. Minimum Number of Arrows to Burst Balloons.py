def solver(points): 
    points.sort()
    print(points)
    count = 1
    prev = points.pop()
    while len(points) != 0: 
        curr = points.pop()
        prev = overlap(curr, prev)
        if not prev: 
            prev = curr 
            count += 1 
    return count 


def overlap(a, b): 
    x = max(a[0], b[0])
    y = min(a[-1], b[-1])
    if x > y: 
        return False 
    return x, y 



points = [[1,6],[1,3],[2,3],[7,12]]


print(solver(points))