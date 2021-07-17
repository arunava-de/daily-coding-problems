# Assuming there are no cycles, we have an inverse topological sort problem here 

def topo_sort_vertex(u, stack, visited, G):

    visited.add(u)

    for v in G[u]:
        if v not in visited:
            topo_sort_vertex(v, stack, visited, G) 

    stack.append(u)

def complete_course(G):

    visited = set()
    stack = []

    for u in G.keys():
        if u not in visited:
            topo_sort_vertex(u, stack, visited, G)
    
    return stack

G = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}

complete_course(G)

G = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC400': ['CSC100', 'CSC200', 'CSC300'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

complete_course(G)