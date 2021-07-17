V = 5
G = {0:set([1,2]), 1:set([2,3]), 3:set([4]), 4:set([1]), 2:set()}

visited = [-1]*V #Takes 3 values: 0, -1 and 1
stack = []

source = 0

def detect_cycle(u, G, visited, stack):

    stack.append(u)
    visited[u] = 0

    for v in G[u]:
        if visited[v]==-1:
            if detect_cycle(v, G, visited, stack):
                return True
        elif visited[v]==0:
            return True
    
    stack.pop()
    visited[u] = 1

    return False

def make_graph(E, V):

    G = {}

    for v in range(V):
        G[v] = set()

    for e in E:
        G[e[0]-1].add(e[1]-1)

    return G


detect_cycle(source, G, visited, stack)

E = [  [1, 2],
        [4, 1],
        [2, 4],
        [3, 4],
        [5, 2], 
        [1, 3] ]
G = make_graph(E, 5)
visited = [-1]*5
stack = []
detect_cycle(0, G, visited, stack)

E = [  [1, 2],
        [2, 3],
        [3, 4], 
        [4, 5] ]

G = make_graph(E, 5)
visited = [-1]*5
stack = []
detect_cycle(0, G, visited, stack)


