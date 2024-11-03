def fib(n):
    li = [0] * (n+1)

    li[0] = li[1] = 1

    for i in range(2, n+1):
        li[i] = li[i-1]+li[i-2]
    
    return li[n-1]

n = int(input())
print(fib(n), n-2)