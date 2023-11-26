from bisect import bisect_left, bisect_right

# logic: 
# initialise a sorted list of nums 
# store previous res and l_bisector, r_bisector 
# if current num == prev num: same res 
# if current num < prev num: 



# Time complexity: 


def solver(nums): 
    l = len(nums)
    # first element 
    diff = 0 
    for i in range(1, len(nums)): 
        diff += nums[i] - nums[0]
    res = [diff] 
    prev = nums[0]
    for i in range(1, len(nums)): 
        if i > 0 and nums[i] == nums[i - 1]: 
            res.append(res[-1])
            continue 
        diff = nums[i] - prev
        # for nums before pre_pos, + abs value 
        # for nums after, - abs value 
        new_val = res[-1] + i * diff - (l - i) * diff 
        res.append(new_val)
        prev = nums[i]
    return res
        



nums = [2,3,5]
nums = [1,4,6,8,10] 
print(solver(nums))