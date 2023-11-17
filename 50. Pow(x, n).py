def myPow(x, n): 
    if n < 0: 
        n = -n 
        x = 1/x 
    if n == 1: 
        return x
    if n == 0: 
        return 1 
    if n % 2 == 1: 
        return x * myPow(x, n - 1)
    if n % 2 == 0: 
        return myPow(x * x, n / 2)
    

print(myPow(2, 10))