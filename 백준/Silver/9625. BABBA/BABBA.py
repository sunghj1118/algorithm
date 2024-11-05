def fib(n):
    # edgecase
    if n == 0:
        return [1,0]
    elif n == 1:
        return [0,1]

    li = [0] * (n+1)
    li[0] = [1,0]
    li[1] = [0,1]
    
    for i in range(2, n+1):
        li[i] = [li[i-1][0] + li[i-2][0], li[i-1][1] + li[i-2][1]]

    return li[n]

result = fib(int(input()))
print(result[0], result[1])