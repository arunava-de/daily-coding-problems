class Graph:
    def __init__(self, vertices, edges):
        self.V = len(vertices)
        self.char_map = {i:vertices[i] for i in range(self.V)}
        self.graph_dict = {}

        for i in range(self.V):
            self.graph_dict[i] = set()

        for e in edges:
            self.graph_dict[e[0]].add(e[1])

    def has_cycles(self, v, visited, stack):

        visited[v] = True 
        stack[v] = True

        for w in self.graph_dict[v]:
            if visited[w] == False:
                if self.has_cycles(w, visited, stack) == True:
                    return True 
            elif stack[w] == True:
                return True 
        
        stack[v] = False 
        return False 

    def has_cycles(self, v):

        visited = [False]*self.V
        S = [v]

        while S:
            u = S.pop()

            for w in self.graph_dict(u):
                if not visited[w]:
                    visited[w] = True 
                    S.append(w)
                else:
                    if w in S:
                        return True 
        
        return False 



