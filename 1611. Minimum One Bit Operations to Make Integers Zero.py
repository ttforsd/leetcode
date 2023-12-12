def solver(n): 
    if n == 1: 
        return 1 
    if n == 0: 
        return 0 
    first = n % 2 
    if first == 0: 
        return 2 + solver(n // 2)
    else: 
        return 1 + solver(n//2)
    

print(solver(8))