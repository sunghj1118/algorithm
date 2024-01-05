def apartment(k, n):
    dp = [[0] * (n+1) for _ in range(k+1)]

    for i in range(k + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j + 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[k][n-1]


t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(apartment(k, n))
