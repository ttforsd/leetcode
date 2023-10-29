from math import inf 

def solver(nums): 
    res = max(nums)
    init = nums.copy()
    init.pop()
    for i in range(1, len(nums)): 
        tmp = [] 
        for j in range(len(init)): 
            tmp.append(init[j] * nums[j + i])
            res = max(res, tmp[-1])
        tmp.pop()
        init = tmp.copy()
    return res
nums = [2,3,-2,4]

print(solver([-2,0,-1]))