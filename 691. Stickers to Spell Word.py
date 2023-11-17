from collections import Counter
from math import inf  
def solver(stickers, target): 
    target = Counter(target)
    tmp = stickers[:]
    stickers = [] 
    for t in tmp:
        holder = Counter(t)
        res = [] 
        for key in target: 
            if key in holder:
                res.append(holder[key])
            else: 
                res.append(0)
        stickers.append(tuple(res))
    tmp = target.copy()
    target = [] 
    for key in tmp: 
        target.append(tmp[key])
    target = tuple(target)
    memo = {} 
    def recur(target):
        if sum(target) == 0: 
            return 0 
        if target in memo: 
            return memo[target]
        res = inf
        for sticker in stickers: 
            tmp = deduction(target, sticker)
            if tmp != target: 
                res = min(res, 1 + recur(tmp))
        memo[target] = res 
        return res 
    res = recur(target)
    if res == inf: 
        return -1 
    return res


def deduction(a, b): 
    res = [] 
    for i in range(len(a)): 
        res.append(max(a[i]-b[i], 0))
    return tuple(res)


stickers = ["with","example","science"]
target = "thehat"

stickers = ["notice","possible"]
target = "basicbasic"

print(solver(stickers, target))