def fib(n):
    if n == 0:
        return 0
    if n==1 or n==2:
        return 1
    
    li = [0] * (n+1)
    li[0] = 0
    li[1] = li[2] = 1

    for i in range(3, n+1):
        li[i] = li[i-1] + li[i-2]
    
    return li[n]

print(fib(int(input())))