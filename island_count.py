class Land:
    def __init__(self, r, c, g):
        self.row = r 
        self.col = c
        self.graph = g

    def is_safe(self, i, j, visited):
        return (i>=0 and i<self.row and j>=0 and j<self.row and not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):

        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

        visited[i][j] = True 

        for k in range(8):
            if self.is_safe(i+rowNbr[k], j+colNbr[k], visited):
                self.DFS(i+rowNbr[k], j+colNbr[k], visited)

    def count_islands(self):

        visited = [[False] * self.col for i in range(self.row)]

        count = 0

        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j]!=True and self.graph[i][j]==1:
                    self.DFS(i, j, visited)
                
                    count += 1

        return count 

graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g = Land(row, col, graph)
 
print("Number of islands is:")
print(g.count_islands())


    