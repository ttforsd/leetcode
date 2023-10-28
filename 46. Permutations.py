def solver(nums): 
    if len(nums) == 1: 
        return [nums][:]
    result = []
    for i in range(len(nums)): 
        tmp = solver(nums[:i] + nums[i + 1:])
        for _ in tmp: 
            _ = _.copy()
            _.append(nums[i])
            result.append(_)
    return result