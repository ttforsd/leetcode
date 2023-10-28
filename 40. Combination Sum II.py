def solver(candidates, target): 
    candidates.sort()
    res = []
    def dfs(i, comb, remain): 
        if remain == 0: 
            res.append(comb[:])
        if remain < 0 or i >= len(candidates): 
            return 
        comb.append(candidates[i])
        if i < len(candidates) and candidates[i+1] != candidates[i]:
            dfs(i + 1, comb, remain - candidates[i])
            comb.pop()
            dfs(i + 1, comb, remain)
    dfs(0, [], target)
    return res


candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30

print(solver(candidates, target))