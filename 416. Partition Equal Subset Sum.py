def solver(nums): 
    total = sum(nums)
    if total % 2 == 1: 
        return False 
    memo = {} 
    def recur(i, remain): 
        if remain == 0: 
            return True 
        if i >= len(nums) - 1: 
            return False 
        if (i, remain) in memo: 
            return memo[(i, remain)] 
        if remain < 0:
            return False 
        result = False 
        for index in (i, len(nums)): 
            result = result or recur(index + 1, remain - nums[i])
            result= result or recur(index + 1, remain)
        memo[(i, remain)] = result 
        return result
    return recur(0, total / 2)
    

nums = [1,2,3,5,7]

print(solver(nums))