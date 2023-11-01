from collections import Counter

def solver(nums): 
    res = 0 
    numsmap = Counter(nums)
    nums = list(set(nums))
    nums.sort()
    dp = [0 for i in range(len(nums))]
    for i in range(len(dp)): 
        if i == 0 or (i == 1 and nums[i] - nums[i-1] == 1): 
            dp[i] = numsmap[nums[i]] * nums[i] 
            res = max(res, dp[i])
        elif nums[i] - nums[i-1] == 1: 
            tmp = 0
            if i > 2: 
                tmp = dp[i - 3]
            dp[i] = numsmap[nums[i]] * nums[i] + max(dp[i-2], tmp)
            res = max(res, dp[i])
        else: 
            dp[i] = numsmap[nums[i]] * nums[i] + max(dp[i-1], dp[i-2])
            res = max(res, dp[i])
    return res


n = [3,4,2]

print(solver(n))