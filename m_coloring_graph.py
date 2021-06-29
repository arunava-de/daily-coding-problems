def is_safe(G, v, cmap, c):

    for i in range(len(G)):
        if G[v][i]==1 and cmap[i]==c: #Checking if neighbors have same color
            return False

    return True

def color_graph(G, v, cmap, k):

    if v==len(G): #We have colored all the vertices
        return True
    
    for c in range(1,k+1):
        if is_safe(G, v, cmap, c):
            cmap[v] = c
            if color_graph(G, v+1, cmap, k):
                return True
            cmap[v] = 0

    return False

graph = [[0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]]

cmap = [0]*len(graph)
k = 3

color_graph(graph, 0, cmap, k)
print(cmap)