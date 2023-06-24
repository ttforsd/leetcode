def solver(s): 
    start = [[s[0]]]
    for i in range(1, len(s)): 
        tmp = []
        for _ in start: 
            tmp.append(_.copy() + [s[i]])
            if _[-1] == s[i]: 
                tmp.append(_[:-1] + [_[-1] + s[i]])
            if len(_) >= 2: 
                if _[-2] == s[i]: 
                    tmp.append(_[:-2] + ["".join(_[-2:]) + s[i]])
        start = tmp.copy()
    return start
        



print(solver("aab"))