def solver(s): 
    if len(s) <= 1: 
        return len(s) 
    l = 0 
    r = 0 
    res = 0 
    chars = set()
    while r < len(s): 
        if s[r] not in chars: 
            chars.add(s[r])
            res = max(res, r - l + 1)
        else: 
            while True: 
                l += 1
                if s[l - 1] == s[r]: 
                    break
                chars.remove(s[l-1])
        r += 1
    return res




def solver0(s, memo = {}):
    if len(s) <= 1: 
        return len(s)
    longest = 0 
    a, b = 0 , 1
    while a + b <= len(s): 
        if checker(s[a:a+b], memo): 
            longest = max(longest, b)
            b +=1 
        else: 
            a += 1
            b -= 1
    return longest

def checker(s, memo):
    if s in memo: 
        return memo[s]
    memo[s] =  len(set(s)) == len(s)
    return memo[s]


s = "tmmzuxt"

# s = "abcabcbb"

print(solver(s))