def max_wine(wines):
    n = len(wines)
    if n <= 2:
        return sum(wines)
    
    dp = [[0]*3 for _ in range(n)]

    # j=0 : current wine not drunk
    # j=1 : current wine drunk, previous wine not drunk
    # j=2 : current wine drunk, previous wine drunk
    
    dp[0][1] = wines[0]
    dp[1][0] = wines[0]
    dp[1][1] = wines[1]
    dp[1][2] = wines[0]+wines[1]

    for i in range(2, n):
        # not drinking current
        dp[i][0] = max(dp[i-1])

        # drinking current, not drinking previous
        dp[i][1] = wines[i] + dp[i-1][0]

        # drinking current and previous
        dp[i][2] = wines[i] + dp[i-1][1]
    
    return max(dp[n-1])

n = int(input())
wines = [int(input()) for _ in range(n)]
print(max_wine(wines))