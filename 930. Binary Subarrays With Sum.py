def solver(nums, goal): 
    lead0 = 0 
    tail0 = 0 
    l = 0 
    r = 0 
    s =  0
    ans = 0 
    while r < len(nums): 
        if nums[l] == 0: 
            lead0 += 1
            l += 1 
            r = max(l, r) 
        elif nums[r] == 1 and s < goal: 
            tail0 = 0
            r += 1 
            s += 1 
        elif nums[r] == 0 and s == goal: 
            tail0 += 1 
            r += 1 
        elif nums[r] == 0: 
            r += 1
        else: 
            ans += (tail0 + 1) * (lead0 + 1) 
            l += 1 
            r = max(l, r)
            s -= 1 
            lead0 = 0 
    if s == goal: 
        ans += (tail0 + 1) * (lead0 + 1) 
    return ans


nums = [0, 0, 1, 0, 1, 0, 0, 1,1] 
nums = [1,0,1,0,1]
goal = 2 

print(solver(nums, goal))


