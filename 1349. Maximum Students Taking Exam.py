def solver(seats): 
    for i in range(len(seats)): 
        for j in range(len(seats[0])): 
            if seats[i][j] == ".": 
                seats[i][j] = [1,1,1]
            if seats[i][j] == "#": 
                seats[i][j] = [0,0,0] 
    for i in range(len(seats)): 
        for j in range(len(seats[0])): 
            if i == 0: 
                if seats[i][j][0] != 0 and j - 1 > 0: 
                    tmp = seats[i][j-2][0]
                    if j - 2 > 0: 
                        tmp = max(tmp, seats[i][j-3][0])
                    seats[i][j][0] += tmp
                    seats[i][j][-1] += tmp 
                if seats[i][j][0] != 0: 
                    seats[i][j][1] = 1 
                elif seats[i][j][0] == 0: 
                    if j - 1 >= 0: 
                        seats[i][j][-1] = seats[i][j-1][-1] 
                continue 
            # calculate height 
            seats[i][j][1] += seats[i-1][j][1]
            if j == 0 and seats[i][j][0] != 0:
                seats[i][j][0] += seats[i-1][j][1]
            if j - 2 == 0 and seats[i][j][0] != 0: 
                seats[i][j][0] += seats[i][j-2][0]
                seats[i][j][0] += seats[i-1][j][1]
            if j == 1 and seats[i][j][0] != 0: 
                seats[i][j][0] = seats[i][j][1]
            if j >= 3 and seats[i][j][0] != 0: 
                seats[i][j][0] += max(seats[i][j-2][0], seats[i][j-3][0])
                seats[i][j][0] += seats[i-1][j][1]
                seats[i][j][-1] += max(seats[i][j-2][-1], seats[i][j-3][-1])
            if seats[i][j][0] == 0 and j == 0: 
                seats[i][j][0] = seats[i][j][1] 
            if seats[i][j][0] == 0 and j == 1: 
                seats[i][j][-1] = seats[i][j-1][-1] 
                seats[i][j][0] = max(seats[i][j][1], seats[i][j-1][0])
            if seats[i][j][0] == 0 and j == 2: 
                seats[i][j][-1] = max(seats[i][j-1][-1], seats[i][j-2][-1])
                seats[i][j][0] = max(seats[i][j-1][0], seats[i][j-2][-1] + seats[i][j][1])
            if seats[i][j][0] == 0 and j >= 3: 
                seats[i][j][-1] = max(seats[i][j-1][-1], seats[i][j-2][-1])
                seats[i][j][0] = max(seats[i][j-1][0], seats[i][j-2][0] + seats[i][j][1], seats[i][j-3][0] + seats[i][j][1])
    for s in seats: 
        print(s)
    return max(seats[-1][-1][0], seats[-1][-2][0])

            
                


seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]


seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
seats = [[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]]

# seats = [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]


for seat in seats: 
    print(seat)

print(solver(seats))