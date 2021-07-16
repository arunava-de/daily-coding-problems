import random 

def rand_excl(n, l):
    num = random.randint(0,n-1)
    while num in l:
        num = random.randint(0,n-1)
    
    return num 

l = [1,4,5,8]
n = 10
counts = {}
for i in range(n):
    counts[i] = 0

for i in range(100000):
    num = rand_excl(n, l)
    counts[num] += 1