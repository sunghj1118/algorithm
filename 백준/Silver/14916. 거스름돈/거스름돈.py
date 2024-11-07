def dp(n):
    if n <= 5:
        return [-1,-1,1,-1,2,1][n]

    li = [0] * (n+2)
    li[0] = -1
    li[1] = -1
    li[2] = 1
    li[3] = -1
    li[4] = 2
    li[5] = 1

    for i in range(6, n+1):
        if li[i-2] != -1 and li[i-5] != -1:
            li[i] = min(li[i-2], li[i-5]) + 1
        elif li[i-2] != -1:
            li[i] = li[i-2] + 1
        elif li[i-5] != -1:
            li[i] = li[i-5] + 1
        else:
            li[i] = -1

    return li[n]

print(dp(int(input())))