def fib(n):
    # edge
    if n <= 1:
        return n

    # setup
    dp = [0] * (n+1)

    # initialize
    dp[0] = 0
    dp[1] = dp[2] = 1
    
    # fill dp table
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib(int(input())))