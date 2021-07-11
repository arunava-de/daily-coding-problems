def col_remove_sort(A):

    N, M = len(A), len(A[0])

    count = 0 

    for j in range(M):
        for i in range(N-1):
            if A[i][j]>A[i+1][j]:
                count += 1
                break
    
    return count 

A = ['cba', 'daf', 'ghi']
print(col_remove_sort(A))

A = ['abcdef']
print(col_remove_sort(A))

A = ['zyx', 'wvu', 'tsr']
print(col_remove_sort(A))