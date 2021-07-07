def max_product(nums):
    max_1 = -10**6
    max_2 = -10**6
    max_3 = -10**6
    min_1 = 10**6
    min_2 = 10**6

    for i in range(len(nums)):
        if nums[i]>max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = nums[i]
        elif nums[i]>max_2:
            max_3 = max_2
            max_2 = nums[i]
        elif nums[i]>max_3:
            max_3 = nums[i]
    
    for i in range(len(nums)):
        if nums[i]<min_1:
            min_2 = min_1
            min_1 = nums[i]
        elif nums[i]<min_2:
            min_2 = nums[i]

    print(max_1,max_2,max_3)
    print(min_1,min_2)
    return max(max_1*max_2*max_3, max_1*min_1*min_2)
    

nums = [-10, -10, 5, 2]
print(max_product(nums))

nums = [10, 3, 5, 6, 20]
print(max_product(nums))

nums = [-10, -3, -5, -6, -20]
print(max_product(nums))

nums = [1, -4, 3, -6, 7, 0]
print(max_product(nums))