def fun(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(str(i)+'*'+str(j)+'='+str(i*j), end=' ')
        print("  ")

print(fun(9))
