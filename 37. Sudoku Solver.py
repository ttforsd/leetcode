def solver(board): 
    incom_cord = check_incomplete(board)
    nums = [str(i) for i in range(1,10)]
    nums = set(nums)
    horizontals = fill_horizontals(board,nums)
    verticals = fill_verticals(board, nums)
    grids = fill_grids(board, nums)
    news = set()
    for i in range(1000):
        news = set()
        for x, y in incom_cord: 
            hor_miss = horizontals[x]
            vert_miss = verticals[y]
            grid_cor = grid_locate((x,y))
            grid_miss = grids[grid_cor]
            poss = hor_miss & vert_miss & grid_miss
            if len(poss) == 1: 
                num = poss.pop()
                news.add((x,y))
                board[x][y] = num
                hor_miss.remove(num)
                vert_miss.remove(num)
                grid_miss.remove(num)
            else: 
                nei_rows = compare(x)
                nei_cols = compare(y)
                nei_rows_values = [] 
                nei_cols_values = []
                for row in nei_rows: 
                    nei_rows_values.append(nums-horizontals[row])
                for col in nei_cols: 
                    nei_cols_values.append(nums-verticals[col])
                nei_comm = nei_cols_values[0] & nei_cols_values[1] & nei_rows_values[0] & nei_rows_values[1]
                poss = poss & nei_comm
                if len(poss) == 1: 
                    num = poss.pop()
                    news.add((x,y))
                    board[x][y] = num
                    hor_miss.remove(num)
                    vert_miss.remove(num)
                    grid_miss.remove(num)
        incom_cord -= news
    for _ in board: 
        print(_)

# take coordinate, return index of rows or columns to compare
def compare(n): 
    tmp = n //3 * 3 
    tmp = [tmp, tmp+1, tmp+2]
    tmp.remove(n)
    return tmp

def grid_locate(coor): 
    i, j = coor
    return i // 3 * 3 + j //3

# given board, return coordinate of incomplete items
def check_incomplete(board):
    indices = set()
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] == '.': 
                indices.add((i,j))
    return indices

def fill_horizontals(board, nums):
    row_missing = []
    for row in board: 
        tmp = set()
        row = set(row)
        for num in nums: 
            if num not in row: 
                tmp.add(num)
        row_missing.append(tmp.copy())
    return row_missing

def fill_verticals(board, nums): 
    col_missing = [] 
    for i in range(9): 
        tmp = set()
        column = set(find_columns(board,i))
        for num in nums: 
            if num not in column: 
                tmp.add(num)
        col_missing.append(tmp.copy())
    return col_missing

def fill_grids(board,nums): 
    grid_missing = [] 
    for i in range(3): 
        for j in range(3): 
            tmp = set()
            grid = set(find_grids(board,(i,j)))
            for num in nums: 
                if num not in grid: 
                    tmp.add(num)
            grid_missing.append(tmp.copy())
    return grid_missing

def find_columns(board, i): 
    result = [board[j][i] for j in range(9)]
    return result


def find_grids(board, cord):
    x,y = cord 
    x *= 3 
    y *= 3
    result = [] 
    for i in range(3): 
        for j in range(3): 
            result.append(board[x+i][y+j]) 
    return result


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]



def main(board): 
    pass 


def isvalid(x, y , value): 
    pass



print(solver(board))