def topo_sort_vertex(v, visited, stack, G):

    visited[v] = True 

    for w in G[v]:
        if not visited[w]:
            topo_sort_vertex(w, visited, stack, G)
    
    stack.append(v)

def topo_sort(V, G):

    visited = [False]*(V+1)
    stack = []

    for v in range(1, V+1):
        if not visited[v]:
            topo_sort_vertex(v, visited, stack, G)

    return stack[::-1]
