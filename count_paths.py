def count_paths(N,M):

    def count(i,j):
        if i>=N or j>=M: #Out of bounds
            return 0
        if i==N-1 and j==M-1:
            return 1 
        elif i==N-1 and j<M-1:
            return count(i,j+1)
        elif i<N-1 and j==M-1:
            return count(i+1,j)
        else:
            return count(i,j+1) + count(i+1,j)
    
    return count(0,0)
        