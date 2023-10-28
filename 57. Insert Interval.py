def solver(intervals, newInterval): 
    switch = False 
    ns, ne = newInterval 
    tmp = [] 
    for s, e in intervals: 
        if switch: 
            if s > tmp[-1][-1]: 
                tmp.append([s, e])
                switch = False 
            else: 
                tmp[-1][-1] = max(e, tmp[-1][-1])
            continue
        if ns > e: 
            tmp.append([s,e])
        elif ne < s: 
            tmp.append([ns, ne])
            tmp.append([s, e])
        elif ne >= s: 
            if ne > e: 
                switch = True 
                tmp.append([s, ne])
            else: 
                tmp.append([ns, e])
        elif s <= ns <= e: 
            if ne <= e: 
                tmp.append([s, e])
            else: 
                switch = True 
                tmp.append([s, ne])
    return tmp


intervals = [[1,5]]

newInterval = [0,6]


print(solver(intervals, newInterval))