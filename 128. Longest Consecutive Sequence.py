def solver(nums): 
    hash = set()
    for num in nums: 
        hash.add(num)
    global_max = 0 
    for num in nums: 
        if num - 1 not in hash: 
            local_max = 1 
            while num + 1 in hash: 
                local_max += 1 
            global_max = max(local_max, global_max)
    return global_max
