def max_sum_subarray(nums):
    prefix_sums = [0]*len(nums)
    prefix_sums[0] = nums[0]

    for i in range(1,len(nums)):
        prefix_sums[i] = prefix_sums[i-1] + nums[i]

    # Max subarray sum will be the max difference in this array, where larger element occurs after smaller

    min_nums = 10**6
    max_sum = -10**6

    for i in range(len(prefix_sums)):
        if prefix_sums[i] < min_nums:
            min_nums = prefix_sums[i]
        
        temp = prefix_sums[i] - min_nums

        if temp>max_sum:
            max_sum = temp

    return max_sum

print(max_sum_subarray([-2,-3,4,-1,-2,1,5,-3]))
