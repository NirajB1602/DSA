# def flood_fill(x, y, new_color, screen, n):    
#     color = screen[x][y]
#     flood_fill_helper(0, 0, color, new_color, screen, n)
            
#     print_sol(screen, n)

# def flood_fill_helper(row, col, color, new_color, screen, n):
#     if row == n - 1 and col == n - 1:
#         return 
    
#     if col == n:
#         row += 1
#         col = 0

#     if screen[row][col] == color:
#         screen[row][col] = new_color
#         flood_fill_helper(row, col + 1, color, new_color, screen, n)
#     else:
#         flood_fill_helper(row, col + 1, color, new_color, screen, n)

# def print_sol(screen, n):
#     print("The new pixels are:")
#     for row in range(n):
#         for col in range(n):
#             print(screen[row][col], end = " ")
#         print()

# screen =[[1, 1, 1, 1, 1, 1, 1, 1], 
#          [1, 1, 1, 1, 1, 1, 0, 0], 
#          [1, 0, 0, 1, 1, 0, 1, 1], 
#          [1, 2, 2, 2, 2, 0, 1, 0], 
#          [1, 1, 1, 2, 2, 0, 1, 0], 
#          [1, 1, 1, 2, 2, 2, 2, 0], 
#          [1, 1, 1, 1, 1, 2, 1, 1], 
#          [1, 1, 1, 1, 1, 2, 2, 1]]

# print("The original pixels are:")
# for row in range(len(screen)):
#     for col in range(len(screen)):
#         print(screen[row][col], end = " ")
#     print()
# print()

# flood_fill(4, 4, 3, screen, len(screen))


def flood_fill(x, y, new_color, screen, n):
    color = screen[x][y]
    flood_fill_helper(x, y, color, new_color, screen, n)
            
    print_sol(screen, n)

def flood_fill_helper(row, col, color, new_color, screen, n):
    if row < 0 or row >= n or col < 0 or col >= n or screen[row][col] != color or screen[row][col] == new_color:
        return
    
    screen[row][col] = new_color

    # Visit neighboring cells
    flood_fill_helper(row + 1, col, color, new_color, screen, n)
    flood_fill_helper(row - 1, col, color, new_color, screen, n)
    flood_fill_helper(row, col + 1, color, new_color, screen, n)
    flood_fill_helper(row, col - 1, color, new_color, screen, n)

def print_sol(screen, n):
    print("The new pixels are:")
    for row in range(n):
        for col in range(n):
            print(screen[row][col], end=" ")
        print()

screen =[
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1]
]

print("The original pixels are:")
for row in range(len(screen)):
    for col in range(len(screen[0])):
        print(screen[row][col], end=" ")
    print()
print()

flood_fill(4, 4, 3, screen, len(screen))
