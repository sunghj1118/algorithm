def staircase(n):
    MOD = 1000000000
    dp = [[0] * 10 for _ in range(n+1)]

    # basecase
    for i in range(1, 10):
        dp[1][i] = 1
    
    # fill table
    for length in range(2, n+1):
        for last_digit in range(10):
            if last_digit == 0:
                dp[length][last_digit] = dp[length-1][1]
            elif last_digit == 9:
                dp[length][last_digit] = dp[length-1][8]
            else:
                dp[length][last_digit] = (dp[length-1][last_digit-1] + dp[length-1][last_digit+1]) % MOD
    
    return sum(dp[n]) % MOD

n = int(input())
print(staircase(n))