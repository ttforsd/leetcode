def solver(mat): 
    filled = set() 
    res = 0 
    for i in range(len(mat)): 
        count = 0 
        for j in range(len(mat[0])): 
            if mat[i][j] == 0: 
                continue 
            tmp = None
            if j not in filled: 
                tmp = j 
                filled.add(j)
            count += 1 
        if count == 1 and tmp != None: 
            valid = True 
            for k in range(i + 1, len(mat)): 
                if mat[k][tmp] == 1: 
                    valid = False 
                    break 
            if valid: 
                res += 1 
    return res
                

print(solver([[1,0,0],[0,1,0],[0,0,1]]))