def solver(s, memo = {}):
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
