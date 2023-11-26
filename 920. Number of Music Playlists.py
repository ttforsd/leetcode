def solver(n, goal, k): 
    if k > n: 
        return 0 
    res = 1 
    offset = 1 
    for i in range(goal): 
        if i < k: 
            res *= (n - i)
        elif i > goal - n + 1: 
            print("fuck", (n - k - offset) )
            res *= (n - k - offset) 
            offset += 1 
        else: 
            res *= (n - k) 
    return res 


def main(n, goal, k): 
    return solver(n, goal, k)

print(solver(2,3,0))