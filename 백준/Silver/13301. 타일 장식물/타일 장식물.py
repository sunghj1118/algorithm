def fib(n):
    if n == 1:
        return 4
    if n == 2:
        return 6
    
    li = [0] * (n+1)
    li[1] = li[2] = 1

    for i in range(3, n+1):
        li[i] = li[i-1] + li[i-2]
    
    return (li[n])*2 + (li[n]+li[n-1])*2

print(fib(int(input())))