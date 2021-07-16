def divide(A, B, Q):

    if A<B:
        return Q, A
    if A==B:
        return Q+1, 0
    else:
        return(divide(A-B, B, Q+1))

A = 14
B = 5
Q, R = divide(A,B,0)
print("Quotient :",Q, "Remainder:",R)

A = 2
B = 8
Q, R = divide(A,B,0)
print("Quotient :",Q, "Remainder:",R)

A = 18
B = 6
Q, R = divide(A,B,0)
print("Quotient :",Q, "Remainder:",R)

    