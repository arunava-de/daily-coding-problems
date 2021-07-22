def interleave(a, x):
    res = []

    for i in range(len(a)):
        res.append(a[:i]+[x]+a[i:])
    
    res.append(a+[x])

    return res

def permutation(a):

    if len(a)==1:
        return [a]
    
    res_temp = [] 
    for p in permutation(a[:-1]):
        res_temp += interleave(p, a[-1])
    
    return res_temp 

a = [1,2,3,4]
print(permutation(a))
print(len(permutation(a)))

