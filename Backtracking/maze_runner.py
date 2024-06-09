# def maze_runner(x, y, maze, n, solution):
#     if x == n-1 and y == n-1:
#         solution[x][y] = 1
#         print(solution)
#         return
    
#     if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or solution[x][y] == 1:
#         return
    
#     solution[x][y] = 1
#     maze_runner(x+1, y, maze, n, solution)
#     maze_runner(x, y+1, maze, n, solution)
#     maze_runner(x-1, y, maze, n, solution)
#     maze_runner(x, y-1, maze, n, solution)
#     solution[x][y] = 0

#     return
    
# def display_solution(maze):
#     n = len(maze)
#     solution = [[0 for j in range(n)] for i in range(n)]
#     maze_runner(0, 0, maze, n, solution)

# n = int(input("Enter the number of rows in maze: "))
# maze = []
# for i in range(n):
#     inp = input(f"Enter the elements of {i+1}th row: ")
#     row = [int(ele) for ele in inp.split()]
#     maze.append(row)

# display_solution(maze)

     
def findPath(m, n):
    visited = [[0 for j in range(n)] for i in range(n)]
    ans = []
    res_str = ""
    isValidPath(0, 0, m, visited, res_str, ans, n)
    return ans
        
def isValidPath(x, y, m, visited, s, ans, n):
    if m[n-1][n-1] == 0:
        return
        
    if x == n - 1 and y == n - 1:
        return ans.append(s)
            
    if x < 0 or y < 0 or x >= n or y >= n or m[x][y] == 0 or visited[x][y] == 1:
        return
            
    visited[x][y] = 1
    isValidPath(x+1, y, m, visited, s+"D", ans, n)
    isValidPath(x, y+1, m, visited, s+"R", ans, n)
    isValidPath(x-1, y, m, visited, s+"U", ans, n)
    isValidPath(x, y-1, m, visited, s+"L", ans, n)
    visited[x][y] = 0

    return 


