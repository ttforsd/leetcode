from collections import defaultdict, deque 


def solver(nums,k): 
    m = max(nums)
    start_index = 0 
    count = deque() 
    res = 0 
    for i, num in enumerate(nums): 
        if num != m: 
            continue 
        count.append(i) 
        if len(count) == k: 
            res += (count[0] - start_index + 1) * (len(nums) - i)
            start_index = count[0] + 1 
            count.popleft()
    return res

def solver0(nums, k): 
    res = 0 
    start_index = 0 
    count = defaultdict(deque) 
    for i, num in enumerate(nums): 
        count[num].append(i)
        while count[num][0] < start_index: 
            count[num].popleft()
        if len(count[num]) == k: 
            res += (count[num][0] - start_index + 1) * (len(nums) - i)
            start_index = count[num][0] + 1
    return res 


nums = [1,3,2,3,3]
k = 2

print(solver(nums, k))