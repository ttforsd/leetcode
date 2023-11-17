def solver(nums): 
    pre = [nums[0]]
    for i in range(1, len(nums)): 
        if nums[i] > pre[-1]: 
            pre.append(nums[i])
            continue 
        if nums[i] < pre[0]: 
            pre[0] = nums[i]
            continue 
        if nums[i] < pre[-1]: 
            for j in range(len(pre) - 1, -1, -1): 
                if nums[i] == pre[j]: 
                    break 
                elif nums[i] > pre[j]: 
                    pre[j + 1] = nums[i]
                    break
    return len(pre)


nums = [5,7,-24,12,13,2,3,12,5,6,35]

print(solver(nums))