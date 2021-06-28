def print_board(grid):

    for i in range(9):
        for j in range(9):
            print(str(grid[i][j]),end = " ")
        print()

def is_valid(grid, row, col, num): #Check if it's safe to put num is give position

    #Check row safety
    for y in range(9):
        if grid[row][y] == num:
            return False
    
    #Check column safety
    for x in range(9):
        if grid[x][col] == num:
            return False

    #Check 3x3 box safety

    start_row = row - row%3
    start_col = col - col%3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True 

def solve_sudoku(grid, row, col):

    if row==8 and col==9: #We've reached the last position, assuming we're traversing horizontally
        return True
    
    if col==9: #Reached last column, so we can move on to next row 
        row += 1
        col = 0

    if grid[row][col]>0: #We have already assigned this position, so we move on horizontally
        return solve_sudoku(grid, row, col + 1)

    for num in range(1,10):

        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid, row, col+1):
                return True
            
        grid[row][col] = 0 #We remove our assignment
    
    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solve_sudoku(grid, 0, 0)):
    print_board(grid)
else:
    print("no solution  exists ")