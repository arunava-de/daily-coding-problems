import math

def is_prime(num):
    if num==1:
        return False 
    elif num==2:
        return True 

    for i in range(2,int(math.sqrt(num))):
        if num%i==0:
            return False 
    
    return True

def prime_sum(num):

    for i in range(1,num//2):
        if is_prime(i) and is_prime(num-i):
            return (i,num-i)
