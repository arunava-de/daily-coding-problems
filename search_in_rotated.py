def search(l, v, start, end):

    if end<start:
        return -1

    mid = (start+end)//2

    if l[mid]==v:
        return mid 
    
    if l[start]<l[mid]: #This half is sorted
        if v>=l[start] and v<l[mid]:
            return search(l, v, start, mid-1)
        else:
            return search(l, v, mid+1, end)
    else: #This half is sorted
        if v>l[mid] and v<=l[end]:
            return search(l, v, mid+1, end)
        else:
            return search(l, v, start, mid-1)
    
search([30, 40, 50, 10, 20], 10, 0, 4)