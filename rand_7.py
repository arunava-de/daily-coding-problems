import numpy as np 

def rand5():
    return np.random.randit(low=1, high=5, size=1)

def rand7():
    x = 5*(rand5() - 1) + rand5()
    
    while x>21:
        x = 5*(rand5() - 1) + rand5()
    
    return x%7 + 1


