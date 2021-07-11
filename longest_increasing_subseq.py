def LIS(nums):

    opt = [0]*len(nums)
    opt[0] = 1 

    for i in range(1,len(nums)):
        temp_max = 0

        for j in range(i):
            if nums[j]<=nums[i]:
                if opt[j]>temp_max:
                    temp_max = opt[j]
        
        opt[i] = max(1, 1 + temp_max)
    
    return opt[len(nums)-1]

nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(nums))

nums = [3, 10, 2, 1, 20]
print(LIS(nums))

nums = [3, 2]
print(LIS(nums))

nums = [50, 3, 10, 7, 40, 80]
print(LIS(nums))

