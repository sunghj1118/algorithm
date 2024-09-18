def max_pay(n, workpay):
    dp = [0] * (n+1)

    for i in range(n-1, -1, -1):
        if i + workpay[i][0] <= n:
            dp[i] = max(workpay[i][1] + dp[i+workpay[i][0]], dp[i+1])
        else:
            dp[i] = dp[i+1]
    return dp[0]

n = int(input())
workpay = [list(map(int, input().split())) for _ in range(n)]
print(max_pay(n, workpay))