from math import inf 

def solver(nums): 
    nums = [-inf] + nums + [-inf]
    l = 1
    r = len(nums) - 2
    while True: 
        m = (l + r) // 2 
        if nums[m - 1] < nums[m] > nums[m + 1]:
            return m - 1
        if nums[m - 1] < nums[m] < nums[m + 1]: 
            l = m + 1
        elif nums[m - 1] > nums[m] > nums[m + 1]: 
            r = m - 1
        else: 
            l = m + 1

            
nums = [1,2]


print(solver(nums))