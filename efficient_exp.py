import time 

def pow(a,b):
    if b==0:
        return 1 
    elif b%2==1:
        return a*pow(a,b-1)
    else:
        p = pow(a,b/2)
        return p*p 

def pow_slow(a,b):
    if b==0:
        return 1 
    return a*pow_slow(a,b-1)
