def pinary(n):
    # setup
    dp = [0] * (n+1)

    # initialize
    dp[1] = 1
    if n > 1:
        dp[2] = 1

    # fill array
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(pinary(int(input())))