def solver(nums): 
    if len(nums) == 0: 
        return [[]]
    n = nums.pop()
    combs = solver(nums)
    result = []
    for comb in combs: 
        result.append(comb)
        result.append(comb + [n])
    return result

