def solver(nums): 
    nums.sort()
    res = [] 
    def dfs(index, current): 
        res.append(current.copy())
        prev = 'a' 
        for i in range(index, len(nums)): 
            if nums[i] != prev: 
                prev = nums[i]
                current.append(nums[i])
                dfs(i + 1, current)
                current.pop()
    dfs(0, [])
    return res


nums = [0,1,1,1,3]

print(solver(nums))