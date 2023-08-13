def solver(nums):
    if len(nums) < 2: 
        return False 
    dp = [False for _ in nums]
    dp = [True] + dp 
    if checker_2(nums[:2]): 
        if len(nums) == 2: 
            return True
        dp[2] = True
    for i in range(3, len(nums) + 1): 
        check_2 = checker_2(nums[i-2:i]) and dp[i-2]
        check_3 = checker_3(nums[i-3:i]) and dp[i-3]
        if check_3 or check_2: 
            dp[i] = True 
    return dp[-1]
def checker_3(nums): 
    a = nums[0]
    return nums == [a, a+1, a+2] or nums == [a,a,a]

def checker_2(nums): 
    return nums[0] == nums[1]
