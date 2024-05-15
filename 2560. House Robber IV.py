from math import inf 

def solver(nums, k):
    if k == 1: 
        return min(nums)
    
    memo = {} 
    final = inf 

    def recur(i, k, m): 
        nonlocal final 
        if k == 0:
            return m 
        
        if i >= len(nums): 
            return inf

        if (i, k, m) in memo: 
            return memo[(i, k, m)]
        
        tmp = max(nums[i], m)

        # not use current 
        res = recur(i + 1, k, m)

        # use current 
        res = min(res, recur(i + 2, k - 1, tmp))

        memo[(i, k, m)] = res 
        final = min(final, res)
        return res 
    
    recur(0, k, 0)
    
    return final
        


nums = [2,3,5,9]
k = 2

nums = [2,7,9,3,1]
k = 2

print(solver(nums, k))