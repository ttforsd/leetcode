def solver(matrix): 
    for i in range(1, len(matrix)): 
        for j in range(len(matrix[0])): 
            if matrix[i][j] != 0: 
                matrix[i][j] += matrix[i-1][j]
    res = 0 
    for row in matrix: 
        res = max(res, area_max(row))
    return res

def area_max(heights): 
    heights.sort(reverse=True)
    res = 0 
    for i, h in enumerate(heights): 
        if h == 0: 
            return res 
        res = max(res, (i + 1) * h)
    return res 


matrix = [[0,0,1],[1,1,1],[1,0,1]]

heights = [1,2,3,4]

matrix = [[1,0,1,0,1]]
matrix = 100000*[[1]]

print(solver(matrix))

