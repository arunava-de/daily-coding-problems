INF = 10**7

def line_cost(words, i, j, m):
    cost = 0

    for k in range(i,j+1):
        cost += len(words[k])
    
    cost += j-i 

    if cost>m:
        return INF # Takes care of overshooting
    else:
        return (m-cost)**2

def break_string(s, m):
    words = s.split()
    opt = [0]*(len(words)+1)
    costs = [[0]*(len(words)+1) for i in range(len(words)+1)]
    words = [''] + words #Takes care of indices
    soln = [0]*(len(words)) #Word break indices

    for j in range(1,len(words)):
        for i in range(1,j+1):
            costs[i][j] = line_cost(words, i, j, m)

    for j in range(1, len(words)):
        opt[j] = INF
        # min_cost = INF

        for i in range(1,j+1):
            if opt[i-1]!=INF and costs[i][j]!= INF and opt[i-1] + costs[i][j]<opt[j]:
            # if opt[i-1] + costs[i][j]<min_cost:
                opt[j] = opt[i-1] + costs[i][j]
                soln[j] = i
        # opt[j] = min_cost
    
    return print_soln(soln, len(words)-1, words) 

def print_soln(soln, n, words):
    k = 0
    if soln[n] == 1:
        k = 1
    else:
        k = print_soln(soln, soln[n] - 1, words) + 1
    # print('Line number ', k, ': From word no. ',
    #                              p[n], 'to ', n)
    for i in range(soln[n],n+1):
        print(words[i],end=" ")
    print()

    return k

s = "the quick brown fox jumps over the lazy dog"
m = 10
break_string(s,m)

s = "aaa bb cc ddddd"
m = 6
break_string(s,m)






