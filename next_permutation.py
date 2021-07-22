def next_permutation(num):
    flag = 0
    N = len(num)

    for i in range(len(num)-1, 0, -1):
        if num[i-1]<num[i]:
            flag = 1
            min_greater_than = 10**9
            min_ind = -1

            for j in range(i,N):
                if num[j]<min_greater_than and num[j]>num[i-1]:
                    min_greater_than = num[j]
                    min_ind = j

            num[i-1], num[min_ind] = num[min_ind], num[i-1]

            num[i:] = sorted(num[i:])

            break 
    
    if flag==1:
        return num 

    return sorted(num)
