# computate difference (diff) between original and rev 
# the other pair should have diff 

def rev(n): 
    res = 0
    while n != 0: 
        res *= 10 
        res += n % 10 
        n //= 10 
    return res


def choose2(n): 
    return n * (n - 1) // 2

def solver(nums): 
    counter = 0
    diffs = {} 
    for n in nums: 
        diff = n - rev(n) 
        if diff not in diffs: 
            diffs[diff] = 0
        diffs[diff] += 1
    for key in diffs: 
        counter += choose2(diffs[key])
    return counter 


ns = [13,10,35,24,76]
print(solver(ns))