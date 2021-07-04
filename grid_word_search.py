def grid_search(word, G):

    strings = [''.join(r) for r in G] #Getting row strings
    n, m = len(G), len(G[0])
    for j in range(m):
        s = ""
        for i in range(n):
            s += G[i][j]
        strings.append(s)

    for s in strings:
        if word in s:
            return True 
    
    return False

G = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

word = "FOAM"

print(grid_search(word,G))
    
