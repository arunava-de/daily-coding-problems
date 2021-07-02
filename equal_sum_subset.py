def partition(nums):
    if sum(nums)%2!=0:
        return False 
    
    target = sum(nums)//2

    def subsetsum(nums, i, t):
        if t==0:
            return True
        elif i==0:
            if nums[i] == t:
                return True
            else:
                return False
        else:
            if nums[i]>t:
                return False
            else:
                return subsetsum(nums, i-1, t) or subsetsum(nums, i-1, t-nums[i])
    
    return subsetsum(nums, len(nums)-1, target)

    