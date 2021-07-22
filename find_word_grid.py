def grid_search(i, j, G, word, R, C, level):

    l = len(word)

    if level==l:
        return True 

    if i<0 or i>R-1 or j<0 or j>C-1:
        return False
    
    if G[i][j] == word[level]:

        temp = G[i][j]
        G[i].replace(G[i][j], "#") #Mark as visited

        res = (grid_search(G, word, i - 1, j, R, C, level + 1) |
               grid_search(G, word, i + 1, j, R, C, level + 1) |
               grid_search(G, word, i, j - 1, R, C, level + 1) |
               grid_search(G, word, i, j + 1, R, C, level + 1))

        G[i].replace(G[i][j], temp)
        return res 
    else:
        return False
    

    


    
