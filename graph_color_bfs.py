def adjacency_to_dict(A):

    G = {}
    
    for i in range(len(A)):
        G[i] = set()

    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j]!=0:
                G[i].add(j)
                G[j].add(i)

    return G

def color_graph(G, v, cmap, k):

    Q = [v]
    visited = []

    maxcolors = 1

    while Q:
        u = Q.pop(0)

        for w in G[u]:
            if cmap[w]==cmap[u]:
                cmap[w] += 1
            
            maxcolors = max(maxcolors, max(cmap[u],cmap[w]))
            if maxcolors>k: #Number of colors used > k
                return False
        
            if w not in visited:
                visited.append(w)
                Q.append(w)
    
    return True


graph = [ [ 0, 1, 1, 1 ],
              [ 1, 0, 1, 0 ],
              [ 1, 1, 0, 1 ],
              [ 1, 0, 1, 0 ] ]

print(adjacency_to_dict(graph))
k = 3
cmap = [1]*len(graph)

if color_graph(adjacency_to_dict(graph), 0, cmap, k):
    print(cmap)
else:
    print("Coloring not possible")







                
        





    
