# consider late first
# then consider ways to sub 0 - 1 absense 


def solver(n): 
    # store total number of Ps so far, grouped by most recent late 
    # [[number of Ps, number of combs]]
    old_comb = [[0,0] for i in range(3)]
    old_comb[0] = [0, 1]
    for i in range(n): 
        new = [[0,0] for i in range(3)]
        # update 0 late row 
        for p, c in old_comb: 
            new[0][0] += p + c 
            new[0][1] += c 
        for j in range(2): 
            p, c = old_comb[j] 
            new[j + 1] = [p, c]
        old_comb = new[:]
    ans = 0 
    for a, b in old_comb: 
        ans += a + b 
    return ans % (10**9 + 7)



def solver0(n):
    old = [[0,0]] # number of Ps, days since last late 
    for i in range(n): 
        new = [] 
        for pres, since_late in old: 
            if since_late < 2: 
                # today late 
                new.append([pres, since_late + 1])
                # today not late
                new.append([pres + 1, 0])
            else: 
                new.append([pres + 1, 0])
        old = new[:]
    all_ps = sum([_[0] for _ in old])
    return len(old) + all_ps
print(solver(93573))


