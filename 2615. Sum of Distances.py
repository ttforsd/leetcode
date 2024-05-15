from collections import Counter, defaultdict

def solver(nums): 
    res = [] 
    after = Counter(nums) 
    before = {}
    pos = defaultdict(list) 
    tmp_res = {} # store prev index, res 
    for i, n in enumerate(nums): 
        pos[n].append(i)

    for k in pos: 
        print(k, get_first(pos[k]))

    for i, n in enumerate(nums): 
        if n not in before: 
            before[n] = 1 
            after[n] -= 1 
            tmp = get_first(pos[n])
            res.append(tmp) 
            tmp_res[n] = (i, tmp)
        else: 
            diff = i - tmp_res[n][0]
            tmp = tmp_res[n][-1] 
            tmp = tmp + diff * before[n] - diff * after[n] 
            before[n] += 1 
            after[n] -= 1 
            res.append(tmp) 
            tmp_res[n] = (i, tmp)
    return res 


def get_first(nums): 
    res = 0 
    for n in nums[1:]: 
        res += n - nums[0] 
    return res 


nums = [1,3,1,1,2]

print(solver(nums))