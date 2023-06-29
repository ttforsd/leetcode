def solver(nums): 
    d = dict()
    result = set()
    for num in nums: 
        if num not in d: 
            d[num] = 1 
        else: 
            d[num] += 1 
    d_l = [] 
    for key in d: 
        d_l.append(key)
    for i in range(len(d_l)):
        key = d_l[i]
        double = False 
        if key == 0 and d[key] >= 3: 
            result.add((0,0,0))
            double = True 
        elif d[key] >= 2: 
            double = True 
        del d[key]
        if double: 
            if -key*2 in d: 
                result.add(tuple(sorted([key, key, -key * 2])))
        for j in range(i+1, len(d_l)): 
            key_2 = d_l[j]
            diff = -key - key_2 
            if diff in d: 
                if diff == key_2 and d[key_2] < 2: 
                    pass 
                else: 
                    result.add(tuple(sorted([key, key_2, diff])))
    result = list(result)
    result = [list(_) for _ in result] 
    return result

print(solver([-2,0,1,1,2,0,0,0]))