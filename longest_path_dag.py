def topo_sort_vertex(v, visited, stack, G):

    visited[v] = True 

    for w in G[v]:
        if not visited[w]:
            topo_sort_vertex(w, visited, stack, G)
    
    stack.append(v)

def topo_sort(V, G):

    visited = [False]*(V)
    stack = []

    for v in range(V):
        if not visited[v]:
            topo_sort_vertex(v, visited, stack, G)
            
    return stack

def longest_path(s, V, E):

    G = {}
    for i in range(V):
        G[i] = set()

    for e in E:
        G[e[0]].add(e[1])

    sorted_V = topo_sort(V, G)

    dist = [-10**9]*V
    dist[s] = 0 
    
    while sorted_V:
        u = sorted_V.pop()
        
        if dist[u]!=-10**9:
            for v in G[u]:
                dist[v] = max(dist[u]+1, dist[v])

    return max(dist)

E = [[0,1], [0,2], [2,1], [1,3], [2,3], [3,3]]

V = 4

for v in range(V):
    print("Source: ",v, ", Path: ", longest_path(v, V, E))








    
    




