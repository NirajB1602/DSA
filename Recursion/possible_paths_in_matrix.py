def print_path(arr):
    for i in arr:
        print(i, end = " ")
    print()

def all_possible_paths_in_matrix(x, y, board, temp = []):
    row_len = len(board[0])
    col_len = len(board)

    if x == row_len - 1 and y == col_len - 1:
        temp.append(board[x][y])
        print_path(temp)
        temp.pop()
        return 
    
    if x < 0 or y < 0 or x > row_len - 1 or y > col_len - 1:
        return
    
    temp.append(board[x][y])
    if y+1 < col_len:   
        all_possible_paths_in_matrix(x, y+1, board, temp)
    if x+1 < row_len:
        all_possible_paths_in_matrix(x+1, y, board, temp)
    temp.pop()

    return

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
all_possible_paths_in_matrix(0, 0, board)


    