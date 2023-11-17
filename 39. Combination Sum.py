def solver(candidates, target): 
    res = [] 
    def recur(i, cur, total): 
        if total == target: 
            print(cur)
            res.append(cur.copy())
            return 
        if total > target or i >= len(candidates): 
            return 
        cur.append(candidates[i])
        recur(i, cur, total + candidates[i])
        cur.pop()
        recur(i + 1 , cur, total)
    recur(0, [], 0)
    return res


def solver1(candidates, target, memo = {}): 
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


print(solver([2,3,6,7], 7))