def solver(rowIndex, memo = {}): 
    if rowIndex in memo: 
        return memo[rowIndex]
    if rowIndex == 0: 
        return [1]
    if rowIndex == 1: 
        return [1,1]
    pre_row = solver(rowIndex - 1)
    new_row = [1]
    for i in range(len(pre_row) -1): 
        new_row.append(pre_row[i] + pre_row[i+1])
    new_row.append(1)
    memo[rowIndex] = new_row
    return new_row

def tb(index): 
    dp = [1,1]
    if index == 0: 
        return [1]
    if index == 1: 
        return [1,1]
    for i in range(index-1): 
        tmp = [] 
        for i in range(len(dp) - 1): 
            tmp.append(dp[i] + dp[i+1])
        tmp.insert(0, 1)
        tmp.append(1)
        dp = tmp[:]
    return dp
        


while True: 
    i = int(input("index"))
    print(tb(i))