def valid_moves(grid, row, col): #Return all the valid tiles the rat can move to
    valid = []
    if row==len(grid)-1 and col<len(grid): #We're at the bottom row
        if grid[row][col+1]==1:
            valid.append('forward')
    elif row<len(grid) and col==len(grid)-1: #We're at the rightmost column
        if grid[row+1][col]==1:
            valid.append('down')
    elif row==len(grid)-1 and col==len(grid)-1: #We're at the destination
        return []
    else: #We're inside the maze
        if grid[row+1][col]==1:
            valid.append('down')
        if grid[row][col+1]==1:
            valid.append('forward')
        
    return valid

def solve_maze(grid, row, col):
    if grid[row][col]==0:
        #We're on an invalid tile
        return False

    if row==len(grid)-1 and col==len(grid)-1: #We're at the destination
        grid[row][col] = 'soln'
        return True
    
    valid = valid_moves(grid, row, col)
    # print(valid)
    if valid==[]: #No valid moves left, backtracking triggered
        return False

    for v in valid:
        if v=='forward':
            if solve_maze(grid, row, col+1):
                grid[row][col] = 'soln'
                return True
        if v=='down':
            if solve_maze(grid, row+1, col):
                grid[row][col] = 'soln'
                return True

    # None of the moves lead to a solution    
    grid[row][col] = 1
    return False

grid = [[1, 0, 0, 0],
[1, 1, 0, 1],
[0, 1, 0, 0],
[1, 1, 1, 1]]

if solve_maze(grid, 0, 0):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j],end=" ")
        print()
else:
    print("Maze can't be solved")

    