# # # filling queen column by column
# # def isSafe(row, col, n, board):

# #     # check for above left diagonals
# #     x_diagonal = row
# #     y_diagonal = col
# #     while x_diagonal >= 0 and y_diagonal >= 0:
# #         if board[x_diagonal][y_diagonal] == 'Q':
# #             return False
# #         x_diagonal -= 1
# #         y_diagonal -= 1

# #     # check for same row
# #     x_row = row
# #     y_col = col
# #     while y_col >= 0:
# #         if board[x_row][y_col] == 'Q':
# #             return False
# #         y_col -= 1

# #     # check for below left diagonal
# #     dup_row = row
# #     dup_col = col
# #     while dup_row < n and dup_col >= 0:
# #         if board[dup_row][dup_col] == 'Q':
# #             return False
# #         dup_row += 1
# #         dup_col -= 1

# #     return True
        
# # def solve_n_queen(col, board, n):
# #     if col == n:
# #         for i in range(n):
# #             for j in range(n):
# #                 if board[i][j] == "0":
# #                     print("-", end = " ")
# #                 else:
# #                     print(board[i][j], end = " ")
# #             print()
# #         print()
# #         return
    
# #     for row in range(n):
# #         if isSafe(row, col, n, board):
# #             board[row][col] = "Q"
# #             solve_n_queen(col + 1, board, n)
# #             board[row][col] = '0'

# # board = [['0', '0', '0', '0'], 
# #          ['0', '0', '0', '0'],
# #          ['0', '0', '0', '0'],
# #          ['0', '0', '0', '0']]

# # solve_n_queen(0, board, 4)


# # filling queen row by row
# def isSafe(row, col, n, board):

#     # check for above left diagonals
#     x_diagonal = row
#     y_diagonal = col
#     while x_diagonal >= 0 and y_diagonal >= 0:
#         if board[x_diagonal][y_diagonal] == 'Q':
#             return False
#         x_diagonal -= 1
#         y_diagonal -= 1

#     # check for same column
#     x_row1 = row
#     y_col1 = col
#     while x_row1 >= 0:
#         if board[x_row1][y_col1] == 'Q':
#             return False
#         x_row1 -= 1

#     # check for above right diagonal
#     dup_row = row
#     dup_col = col
#     while dup_row >= 0 and dup_col < n:
#         if board[dup_row][dup_col] == 'Q':
#             return False
#         dup_row -= 1
#         dup_col += 1

#     return True
        
# def solve_n_queen(row, board, n):
#     if row == n:
#         for i in range(n):
#             for j in range(n):
#                 if board[i][j] == "0":
#                     print("-", end = " ")
#                 else:
#                     print(board[i][j], end = " ")
#             print()
#         print()

#         return
    
#     for col in range(n):
#         if isSafe(row, col, n, board):
#             board[row][col] = "Q"
#             solve_n_queen(row + 1, board, n)
#             board[row][col] = '0'

# board = [['0', '0', '0', '0'], 
#          ['0', '0', '0', '0'],
#          ['0', '0', '0', '0'],
#          ['0', '0', '0', '0']]

# solve_n_queen(0, board, 4)
        
def nQueen(n):
        # code here
    board = [[0 for j in range(n)] for i in range(n)]
    sol = []
    def isSafe(row, col, board, n):
        x1 = row
        y1 = col
        while y1 >= 0:
            if board[x1][y1] == 1:
                return False                
            y1 -= 1
            
        x = row
        y = col
        while x >= 0 and y >= 0:
            if board[x][y] == 1:
                return False
                    
            x -= 1
            y -= 1
                
        dup_x = row
        dup_y = col
        while dup_x < n and dup_y >= 0:
            if board[dup_x][dup_y] == 1:
                return False
                
            dup_x += 1
            dup_y -= 1
            
        return True
            
    def solve(col, board, n, temp, sol):
        if col == n:
            print(board)
            return
                
        for row in range(n):
            if isSafe(row, col, board, n):
                board[row][col] = 1
                # temp.append(row)
                solve(col + 1, board, n, temp, sol)
                board[row][col] = 0
                # temp.pop()
                
                
    solve(0, board, n, [], sol)
    # return board

nQueen(4)      