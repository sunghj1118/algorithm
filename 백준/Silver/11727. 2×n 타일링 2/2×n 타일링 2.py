def squares(n):
    if n < 2:
        return [1,3][n-1]
    dp = [0] * (n+1)
    dp[1] = 3
    dp[2] = 5

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
    
    return dp[n-1]


n = int(input())
print(squares(n))