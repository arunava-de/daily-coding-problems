def find_non_dup(A):
    counts = dict()
    for a in A:
        if a in counts.keys():
            counts[a] += 1
        else:
            counts[a] = 1
    
    for a in counts.keys():
        if counts[a] == 1:
            return a