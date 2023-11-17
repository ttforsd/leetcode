def solver(s, p): 
    s += 'a'
    p += 'a'
    memo = {} 
    sl = len(s)
    pl = len(p)

    def compare(a, b): 
        if a == b: 
            return True 
        if a == "." or b == ".": 
            return True 
        return False 

    def recur(i, j): 
        if (i, j) in memo: 
            return memo[(i, j)]
        if i == sl and j == pl: 
            return True 
        if i == sl or j == pl: 
            return False 
        # set default result to false 
        res = False 
        # if next char is * for s 
        switch = True 
        if i < sl - 1 and s[i+1] == "*": 
            switch = False 
            # skip current char and *, without matching j 
            res = res or recur(i + 2, j)
            if res: 
                memo[(i,j)] = True 
                return True
            # if match, match, but not go ahead for s 
            if compare(s[i], p[j]): 
                res = res or recur(i, j + 1)
                if res: 
                    memo[(i,j)] = True 
                    return True 
        if j < pl - 1 and p[j+1] == "*": 
            switch = False 
            # skip current char and *, without matching i 
            res = res or recur(i, j + 2)
            if res: 
                memo[(i,j)] = True 
                return True
            # if match, match, but not go ahead for p 
            if compare(s[i], p[j]): 
                res = res or recur(i + 1, j)
                if res: 
                    memo[(i,j)] = True 
                    return True 
        if switch: 
            if compare(s[i], p[j]): 
                res = res or recur(i + 1, j + 1)
        memo[(i,j)] = res 
        return res 
    return recur(0,0)
        

s = "aa"
p = "a*"


# s = "aac"
# p = ".*b"

print(solver(s, p))