def partition(nums):
    if sum(nums)%2!=0:
        return False 
    
    target = sum(nums)//2

    opt = [[False]*(target+1) for i in range(len(nums)+1)]

    for i in range(len(nums)+1):
        opt[i][0] = True 
    
    for i in range(1, target+1):
        opt[0][i] = True

    for i in range(1,len(nums)+1):
        for t in range(1,target+1):
            if nums[i-1]>t:
                opt[i][t] = opt[i-1][t]
            else:
                opt[i][t] = opt[i-1][t] or opt[i-1][t-nums[i]]

    return opt[len(nums)][target]

    


    