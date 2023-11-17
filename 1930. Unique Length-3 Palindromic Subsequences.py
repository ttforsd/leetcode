from collections import Counter
def solver(s): 
    res = set() 
    c_pos = {} 
    for i in range(len(s)): 
        if s[i] not in c_pos: 
            c_pos[s[i]] = [] 
        c_pos[s[i]].append(i)
    for i, c in enumerate(s[1:len(s) - 1]): 
        i += 1
        for char in c_pos: 
            if c_pos[char][0] < i < c_pos[char][-1]: 
                res.add((c, char))
    return len(res)





s = "aabca" 



print(solver(s))