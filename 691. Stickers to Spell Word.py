from collections import Counter

def solver(stickers, target): 
    return Counter(target)


def deduction(a, b): 
    res = [] 
    for i in range(len(a)): 
        res.append(min(a-b, 0))
    return tuple(res)


stickers = ["with","example","science"]
target = "thehat"

print(solver(stickers, target))