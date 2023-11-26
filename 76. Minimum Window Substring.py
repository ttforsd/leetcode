from collections import deque, Counter, defaultdict
from math import inf

def solver(s, t): 
    l = len(t)
    if len(t) > len(s): 
        return ""
    # store length and starting index in result
    res = (inf, None)
    # if full, remove smallest index 
    # store indexes in a minheap (index, char)? 
    # remove until still valid, then remove 1 further
    t = Counter(t)
    order = deque()
    cache = defaultdict(int)
    for i in range(len(s)): 
        if s[i] not in t: 
            continue 
        order.append(i)
        cache[s[i]] += 1 
        while isValid(cache, t): 
            start = order[0]
            res = min(res, (i - start, start))
            if cache[s[start]] >= t[s[start]]: 
                order.popleft()
                cache[s[start]] -= 1
    if res[0] == inf: 
        return ""
    return s[res[-1]: res[-1] + res[0] + 1] 
            
def isValid(a, target): 
    for key in target: 
        if key not in a: 
            return False
        if a[key] < target[key]: 
            return False 
    return True 




    
s = "ADOBECODEBANC"
t = "ABC"


s = "a"
t = "b"

print(solver(s,t))