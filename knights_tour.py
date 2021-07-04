def is_valid_move(m,n):

    if m[0]>=0 and m[1]>=0 and m[0]<n and m[1]<n:
        return True

    return False

def solution(i, j, B, visited): #Current position, current board and number of tiles visited

    # B[i][j] = visited

    if visited==len(B)**2:
        # print("Reached a solution")
        # B[i][j] = 0 #Backtracking before counting the solution
        return 1

    moves = [(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1),(i-1,j-2),(i+1,j-2),(i-1,j+2),(i+1,j+2)]
    soln = 0

    for m in moves:
        if is_valid_move(m,len(B)) and B[m[0]][m[1]]==0:
            B[m[0]][m[1]] = 1
            soln += solution(m[0], m[1], B, visited+1)
            B[m[0]][m[1]] = 0

    # B[i][j] = 0
    
    return soln

B = [[0]*5 for i in range(5)]
B[0][0] = 1

print(solution(0, 0, B, 1))
    