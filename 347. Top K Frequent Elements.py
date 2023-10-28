from math import inf

def solver(nums, k): 
    result = []
    hashTable = {} 
    for num in nums: 
        if num not in hashTable: 
            hashTable[num] = 0
        hashTable[num] += 1 
    freq = [[] for i in range(len(nums) + 1)]
    for key in hashTable: 
        freq[hashTable[key]].append(key)
    while len(result) < k: 
        tmp = freq.pop()
        for _ in tmp: 
            result.append(_)
    return result
    

nums = [1]

k = 1


print(solver(nums, k))