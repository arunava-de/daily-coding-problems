def make_balanced(arr):

    count = 0

    S = []

    for i in range(len(arr)):
        if S==[]:
            if arr[i]=="(":
                S.append(arr[i])
            else:
                count += 1
                continue 
        else:
            top = S[-1]
            if arr[i]==")":
                S.pop()
                continue 
            else:
                S.append(arr[i])
    
    if S==[]:
        return count 
    else:
        return count + len(S)

arr = "()())()"
print(make_balanced(arr))

arr = ")("
print(make_balanced(arr))

arr = "(((((("
print(make_balanced(arr))

arr = "))))))("
print(make_balanced(arr))

arr = ")())))(())))()"
print(make_balanced(arr))