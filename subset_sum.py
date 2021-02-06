def subset_sum(S, k):
    
    DP = [[False for i in range(k+1)] for j in range(len(S)+1)]

    for i in range(len(S)+1):
        DP[i][0] = True # Always a subset till i-th position with sums to 0, we don't pick anything

    for i in range(1,k+1):
        DP[0][i] = False # Can't pick no elements and expect it to sum to a non-zero number

    for i in range(1,len(S)+1):
        for j in range(1,k+1):
            if S[i-1] > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] or DP[i-1][j-S[i-1]]
    
    if DP[len(S)][k] == False:
        return -1

    # Now we need to do backtracking to figure out solution

    res = []
    temp = k

    for j in range(len(S)-1,-1,-1):
        if S[j]>temp:
            continue
        if DP[j][temp-S[j]]==True:
            res.append(S[j])
            temp -= S[j]
    
    if temp==0:
        return res
    else:
        return -1
    
    return res

print(subset_sum([2,4,6,5,1], 2))


    