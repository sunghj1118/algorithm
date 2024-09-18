def padovan(n):
    if n <= 5:
        return [1,1,1,2,2][n-1]
    dp = [0] * (n+1)
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2

    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    return dp[n]

cases = int(input())
for _ in range(cases):
    n = int(input())
    print(padovan(n))
