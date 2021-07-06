import math

def dfs(u, G, visited, temp):
    visited[u] = True 
    temp.append(u)

    for v in G[u]:
        if visited[v]==False:
            dfs(v, G, visited, temp)
    
    return temp


def count_attacks(bishops, M):
    N = len(bishops)

    G = {}

    for i in range(N):
        G[i] = set()

    for i in range(N-1):
        for j in range(i+1,N):
            b1 = bishops[i]
            b2 = bishops[j]

            if abs(b1[0]-b2[0])==abs(b1[1]-b2[1]): #Lying on the same diagonal
                G[i].add(j)
                G[j].add(i)

    visited = [False]*len(G)
    conn_comps = []

    for u in range(N):
        if visited[u]==False:
            conn_comps.append(len(dfs(u, G, visited, [])))

    res = 0

    for c in conn_comps:
        if c>1:
            res += math.comb(c,2)

    return res

bishops = [(0, 0), (2, 2), (1, 1), (4, 4)]
M = 5
 
print(count_attacks(bishops, M))


    
    