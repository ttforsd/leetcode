from collections import deque 
from math import inf

def distance(x1, y1, x2, y2): 
    return abs(x1 - x2) + abs(y1 - y2)

def solver(sx, sy, fx, fy, t): 
    if sx == fx and sy == fy and t == 1: 
        return False 
    x_diff = abs(sx - fx)
    y_diff = abs(sy - fy)
    diagonals = min(x_diff, y_diff)
    remain = max(x_diff, y_diff) - diagonals 
    if remain + diagonals <= t: 
        return True 
    return False

sx = 2
sy = 4
fx = 7
fy = 7
t = 6


sx = 1
sy = 1
fx = 2
fy = 1
t = 2

print(solver(sx, sy, fx, fy, t))