def min_steps(targets):

    minstep = 0

    for i in range(1,len(targets)):
        source = targets[i-1]
        destination = targets[i]

        diag = min(abs(source[0]-destination[0]), abs(source[1]-destination[1]))

        temp = [None, None]
        temp[0] = source[0] + diag 
        temp[1] = source[1] + diag 

        minstep += diag + max(abs(temp[0]-destination[0]), abs(temp[1]-destination[1]))

    return minstep