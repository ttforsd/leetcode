def solver(candidates, target, memo = {}): 
    if target == 0: 
        return [[]]
    if target in memo: 
        print("memo used")
        return memo[target]
    result = []
    for i in range(len(candidates)): 
        if target - candidates[i] >= 0: 
            tmp = solver(candidates[i:], target - candidates[i])[:]
            for _ in tmp: 
                _ = _.copy()
                _.append(candidates[i])
                result.append(_)
    return result 
