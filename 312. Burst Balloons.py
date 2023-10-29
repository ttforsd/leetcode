def solver(nums):
    tmp = []
    for num in nums: 
        if num > 0: 
            tmp.append(num)
    nums = tuple(tmp)
    memo = {}
    def recur(nums):
        if len(nums) == 1:
            return nums[0]
        if nums in memo:
            print("used")
            return memo[nums]
        result = 0
        for i in range(len(nums)):
            tmp = recur(nums[:i] + nums[i+1:])
            if 0 < i < len(nums) - 1:
                val = nums[i-1] * nums[i] * nums[i + 1]
            if i == 0 and len(nums) == 1:
                val = nums[i]
            if i == 0:
                val = nums[i] * nums[i + 1]
            if i == len(nums) - 1:
                val = nums[i] * nums[i - 1]
            result = max(result, tmp + val)
        memo[nums] = result
        return result
    return recur(nums)

nums = [3,1,5,8]

nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2,9]

# nums = [3,1,5,8,6,7,8,4,5,6,4,5,6,4,56,4,1,2,3,4,5]


print(solver(nums))