def dp(n):
    if n == 1:
        return 3
    if n == 2:
        return 7


    li = [0] * (n + 1)
    li[0] = [2,3]
    li[1] = [5,7]
    li[2] = [12,17]

    for i in range(3, n+1):
        li[i] = [(li[i-1][0]+li[i-1][1]) % 9901,
                 (li[i-1][0]*2+li[i-1][1]) % 9901]

    return li[n-1][1]

print(dp(int(input())))