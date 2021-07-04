def make_fair():

    v1, v2 = foo(), foo()

    if v1 ^ v2: #Exclusive or
        return v1

    return make_fair()
    