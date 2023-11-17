def helper(a, b): 
    if ord(a) - ord(b) == 1: 
        return True
    if a == "a" and b == "z": 
        return True 
    return False 

def solver(s): 
    if len(s) == 1: 
        return 1 
    all_comb = set() 
    l = 0 
    r = 1
    tmp_s = s[0]
    while r < len(s): 
        if helper(s[r], s[r-1]): 
            tmp_s += s[r]
        else: 
            all_comb.add(tmp_s)
            l = r 
            tmp_s = s[l]
        r += 1 
    all_comb.add(tmp_s)
    return all_comb






print(solver("abcabcabcbc"))
