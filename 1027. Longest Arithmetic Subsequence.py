# table: longest desc, dongest asc, desc as of now, asc as of now 

def solver(nums): 
    l = len(nums)
    if l == 2: 
        return l 
    if l < 2: 
        return 1 
    longest = 2
    dp = [{} for _ in nums]
    for i in range(len(nums)): 
        for j in range(i): 
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            longest = max(longest, dp[i][diff])
    return longest 


print(solver([20,1,15,3,10,5,8]))