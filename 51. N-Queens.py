def solver(n): 
    res = [] 
    pre_pos = [] 
    def bt(index): 
        if index == n: 
            res.append(pre_pos.copy())
        invalid = set() 
        for i, a in enumerate(pre_pos): 
            invalid.add(a)
            invalid.add(a + (index - i))
            invalid.add(a - (index - i))
        for i in range(n): 
            if i not in invalid: 
                pre_pos.append(i)
                bt(index + 1) 
                pre_pos.pop()
    bt(0)
    board = [] 
    for r in res: 
        board.append([])
        for i in range(n): 
            board[-1].append("")
            for j in range(n): 
                if r[i] == j: 
                    board[-1][-1] += "Q"
                else: 
                    board[-1][-1] += "."
    return board            
print(solver(9))