from collections import deque

def solver(board, word): 
    def bfs(i, j): 
        queue = deque()
        queue.append((i, j, word, set()))
        while len(queue) != 0: 
            cur_i, cur_j, cur_word, visited = queue.popleft()
            cur_char = board[cur_i][cur_j]
            if cur_char != cur_word[0]: 
                continue 
            if (cur_i, cur_j) in visited: 
                continue 
            visited.add((cur_i, cur_j))
            if len(cur_word) == 1 and cur_word == board[cur_i][cur_j]: 
                return True 
            for _ in [1, -1]: 
                next_i = cur_i + _ 
                next_j = cur_j + _ 
                if 0 <= next_i < len(board): 
                    queue.append((next_i, cur_j, cur_word[1:], visited.copy()))
                if 0 <= next_j < len(board[0]): 
                    queue.append((cur_i, next_j, cur_word[1:], visited.copy()))
        return False
            
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if bfs(i,j): 
                return True 
    return False 


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCCED"


board = [["a"]]
word = "a"


print(solver(board, word))