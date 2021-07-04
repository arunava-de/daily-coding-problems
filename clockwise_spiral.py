def print_spiral(A, r_start, r_end, c_start, c_end):

    if r_start>=r_end or c_start>=c_end:
        return 
    
    for j in range(c_start,c_end):
        print(A[r_start][j])
    
    for i in range(r_start+1,r_end):
        print(A[i][c_end-1])

    if r_end-1!=r_start:
        for j in range(c_end-2,c_start,-1):
            print(A[r_end-1][j])
    
    if c_end-1!=c_start:
        for i in range(r_end-1,r_start,-1):
            print(A[i][c_start])
    
    print_spiral(A,r_start+1,r_end-1,c_start+1,c_end-1)

A = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

print_spiral(A,0,4,0,5)