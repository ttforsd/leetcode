from math import inf 
from collections import deque 


def helper(a, b): 
    if abs(ord(a) - ord(b)) <= 1: 
        return True 
    return False 

def solver(word): 
    if len(word) <= 1: 
        return 0 
    # 2 options, change first or second 
    # if prev changed, then current no need change 
    # if pre not chance and too sim, then need change 
    memo = {} 

    def recur(i): 
        if i >= len(word) - 1: 
            return 0 
        if i in memo: 
            return memo[i] 
        res = inf 
        if helper(word[i], word[i + 1]): 
            if i + 2 < len(word): 
                res = min(res, 1 + recur(i + 2))
            res = min(res, 1 + recur(i + 1))
        else: 
            res = min(res, recur(i + 1))
            if i + 2 < len(word): 
                res = min(res, 1 + recur(i + 2))
        memo[i] = res 
        return res 
    return recur(0)



word = "zyxyxyz"

print(solver(word))

