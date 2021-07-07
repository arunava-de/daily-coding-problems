def nth_perfect(n):
    if n==1:
        return 19
    else:
        return 19+(n//9)*9+(n-1)*9

def is_perfect(num):
    sum = 0
    while num>0:
        sum += num%10
        num = num//10
    
    if sum==10:
        return True 
    return False

def nth_perfect_slow(n):
    c = 0
    num = 1
    while c<n:
        if is_perfect(num):
            c += 1
        num += 1
    
    return num-1