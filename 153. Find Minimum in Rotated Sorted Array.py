def solver(nums):
    # target: find pivot point, using binary search? 
    if len(nums) <= 2: 
        return min(nums)
    if nums[-1] < nums[-2]: 
        return nums[-1] 
    if nums[0] < nums[-1]: 
        return nums[0]
    l = 0 
    r = len(nums) - 1
    while True: 
        m = (l + r) // 2
        # condition where m is ans
        if nums[m - 1] > nums[m] < nums[m + 1]: 
            return nums[m]
        if nums[l] < nums[0]: 
            return nums[l] 
        if nums[m] > nums[l] or m == l: 
            l = m + 1 
        else: 
            r = m - 1 
nums = [4,5,6,7,0,1,2]
nums = [2,3,4,5,1]
nums = [11,13,15,17]
nums = [5,1,2,3,4]
print(solver(nums))