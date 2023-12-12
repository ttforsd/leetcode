def solver(nums): 
    ans = set() 
    nums = tuple(nums)

    def bt(perm, nums): 
        if len(nums) == 0: 
            ans.add(perm) 
        for i in range(len(nums)): 
            bt(perm + tuple([nums[i]]), nums[:i] + nums[i + 1:])
    bt((), nums)
    return [list(_) for _ in ans]


nums = [1,2,3,4,5,6,7,8]

print(solver(nums))


