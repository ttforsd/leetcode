def solver(nums, target): 
    nums.sort()
    ans = [] 
    for i in range(len(nums)): 
        if i != 0 and nums[i] == nums[i - 1]: 
            continue 
        tmp = three_left(nums[i + 1:], target - nums[i]) 
        if tmp != []: 
            for j in range(len(tmp)): 
                tmp[j] = [nums[i]] + tmp[j]
            ans += tmp.copy()
    return ans

def three_left(nums, target): 
    ans = [] 
    for i in range(len(nums)): 
        if i != 0 and nums[i] == nums[i - 1]: 
            continue 
        tmp = two_left(nums[i + 1:], target - nums[i]) 
        if tmp != []: 
            for j in range(len(tmp)): 
                tmp[j] = [nums[i]] + tmp[j]
            ans += tmp.copy()
    return ans

def two_left(nums, target):
    left = 0 
    right = len(nums) - 1
    res = [] 
    while left < right: 
        if nums[left] + nums[right] == target: 
            res.append([nums[left], nums[right]]) 
            left += 1
            while left < len(nums) - 1 and nums[left] == nums[left - 1]: 
                left += 1 
        if nums[left] + nums[right] > target: 
            right -= 1 
        else: 
            left += 1         
    return res



nums = [-2,-1,-1,1,1,2,2]
target = 0

print(solver(nums, target))