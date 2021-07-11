def multiplication_table(N, X):

    count = 0 

    if N>=X:
        count = 2

    for i in range(2,N):
        if X%N==0:
            count += 1
    
    return count
