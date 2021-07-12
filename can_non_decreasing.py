def make_non_decreasing(nums):

    count = 0
    nums = [-10**9] + nums + [10**9] #Take care of boundaries

    for i in range(1,len(nums)-1):
        if nums[i-1]<=nums[i]:
            if nums[i+1]<nums[i]:
                if nums[i+1]>=nums[i-1]:
                    count += 1
                    nums[i] = (nums[i-1]+nums[i+1])/2
        else:
            if nums[i]>nums[i+1]:
                return False
            elif nums[i+1]>nums[i]:
                if nums[i+1]>=nums[i-1]:
                    nums[i] = (nums[i-1]+nums[i+1])/2
                    count += 1
                else:
                    return False
            else:
                return False

    if count<=1:
        return True

    return False

        
nums = [4,2,3]
print(make_non_decreasing(nums))

nums = [4,2,1]
print(make_non_decreasing(nums))