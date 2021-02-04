def find_non_dup(nums):

    # Solution for positive numbers
    # Sum bits for each positiona cross the list, one which doesn't sum to 1
    N = 32 # Max number of bits in int data type
    result = 0

    for i in range(N): # We iterate through the positions

        sm = 0 # Sum of i-th bit
        x = (1 << i) # Used to check if i-th bit is 1 or not

        for j in range(len(nums)):
            if x & nums[j]: # Checks if i-th bit is 1
                sm = sm + 1
            
        if sm % 3!=0: # We get bit of i-th position of answer
            result = result | x

    return result

print(find_non_dup([1,4,4,4,1,1,2]))