def sudoku_solver(x, y, board, n):
    if x >= n and y >= n:
        return True

    for row in range(n):
        for col in range(n):
            if board[row][col] != 0:
                continue
            else:
                for i in range(1, n+1):
                    if isValid(i, row, col, board, n):
                        board[row][col] = i
                        if sudoku_solver(row, col, board, n):
                            return True
                        board[row][col] = 0
                return False
    return True
                    
def isValid(num, row, col, board, n):
    for i in range(n):
        if board[row][i] == num:
            return False
        
        if board[i][col] == num:
            return False
        
    start_row = row - row % 3
    start_col = col - col % 3
    for j in range(3):
        for k in range(3):
            if board[start_row + j][start_col + k] == num:
                return False
            
    return True

def printSolution(board):
    for row in board:
        for ele in row:
            print(ele, end = " ")
        print()

n = 9
board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(sudoku_solver(0, 0, board, n))
printSolution(board)
