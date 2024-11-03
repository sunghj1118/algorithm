def dp(n):
    # edge case
    if n == 0:
        return 1
    
    # base case
    li = [0] * (n+1)
    li[0] = li[1] = 1

    # calculate
    for i in range(2, n+1):
        li[i] = li[i-1] + li[i-2]

    return li[n]

n = int(input())

for i in range(n):
    print(dp(int(input())))