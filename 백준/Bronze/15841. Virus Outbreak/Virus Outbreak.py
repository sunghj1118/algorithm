def cows(n):
    # edge
    if n <= 1:
        return n
    
    # base
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

hr = 0
while True:
    hr = int(input())
    if hr == -1:
        break

    print("Hour " + str(hr) + ": " + str(cows(hr)) + " cow(s) affected")