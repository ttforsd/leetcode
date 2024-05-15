# store local max 
# use local max to update global max 
# if 0, continue 
# for each continuous 1s in each row, use the stack approach to compute max area 
    # modified data structure: change 1s to (current max depth), store and append to separate list, if zero, append 0 
# write separate maxarea function, takes in the list 



# [2,3,2,1,5]

# find choking points 
# cur height >= max in stack, compute max sum (cur index - stack index) * height
# else: pop the 


def solver1(matrix): 
    res = 0 
    dp = {}
    for i, row in enumerate(matrix): 
        for j, n in enumerate(row): 
            if n != "1": 
                continue 
            # check if left exist
            dp[(i, j)] = []
            if (i, j - 1) in dp: 
                left_most = dp[(i, j -1)][-1][1] 
            else: 
                left_most = j 
            if (i - 1, j) in dp: 
                for x, y in dp[(i-1, j)]: 
                    if dp[(i, j)] and y >= dp[(i, j)][-1][-1]:  
                        continue
                    y = max(left_most, y)
                    res = max(res, (i - x + 1) * (j - y + 1)) 
                    dp[(i,j)].append((x, y))
            res = max(res, j - left_most + 1)
            dp[(i, j)].append((i, left_most))
    return res 



def area_max(heights): 
    res = 0 
    heights.append(0) 
    stack = [] # cur largest on the end
    for i, h in enumerate(heights): 
        if len(stack) == 0: 
            stack.append((h, i))
            continue 
        if h >= stack[-1][0]: 
            stack.append((h, i))
            continue 
        while len(stack) > 0 and h < stack[-1][0]: 
            tmp_h, tmp_i = stack.pop() 
            res = max(res, tmp_h * (i - tmp_i))
        stack.append((h, tmp_i))
    return res 
        


def solver(matrix): 
    res = 0 
    for i in range(len(matrix)): 
        heights = [] 
        for j in range(len(matrix[0])): 
            if i == 0: 
                if matrix[i][j] != "0": 
                    matrix[i][j] = int(matrix[i][j])
                    heights.append(1)
                else: 
                    heights.append(0)
                continue 
            if matrix[i][j] == "0": 
                heights.append(0)
                continue 
            if matrix[i-1][j] == "0": 
                heights.append(1) 
                matrix[i][j] = 1
            else: 
                h = 1 + matrix[i-1][j]
                matrix[i][j] = h
                heights.append(h) 
        res = max(res, area_max(heights))
    return res



matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
heights = [2, 1, 2]

# print(solver(matrix))


# print(area_max(heights))
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

matrix = [["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]



print(solver1(matrix))