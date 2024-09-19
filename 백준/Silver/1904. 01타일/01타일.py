def zero_one_tile(n):
    # edge
    if n <= 2:
        return n

    # setup
    dp = [0] * (n+1)

    # initialize
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 15746
    return dp[n]

print(zero_one_tile(int(input())))