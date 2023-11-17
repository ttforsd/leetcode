from collections import deque

def solver(n, left, right): 
    t = 0 
    left.sort(reverse=True)
    right.sort()
    while left and left[-1] == 0: 
        left.pop()
    while right and right[-1] == n: 
        right.pop()
    while len(left) + len(right) != 0: 
        t += 1
        if left: 
            left[-1] -= 1 
            if left[-1] <= 0: 
                left.pop()
                if left: 
                    left[-1] -= t
        if right: 
            right[-1] += 1
            if right[-1] >= n: 
                right.pop()
                if right: 
                    right[-1] += t
    return t 


n = 4
left = [4,3]
right = [0,1]


n = 7
right = [0,1,2,3,4,5,6,7]
left = []

# n = 11
# left = [1,4,5,10,9]
# right = [2,7,6,3]

# n = 9 
# left = [5]
# right = [4]

print(solver(n, left, right))