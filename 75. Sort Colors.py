def solver(nums): 
    i = 0 
    shift = 0 
    for i in range(len(nums)): 
        if nums[i + shift] == 0: 
            del nums[i + shift] 
            nums.insert(0, 0)
        elif nums[i + shift] == 2: 
            del nums[i + shift] 
            shift -= 1 
            nums.append(2)
    return nums 


nums = [2,0,2,1,1,0] 

print(solver(nums))