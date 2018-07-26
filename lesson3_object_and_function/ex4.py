def fun(n):
    return lambda m:n**m
 

A = fun(3)
B = A(5)
print(B)