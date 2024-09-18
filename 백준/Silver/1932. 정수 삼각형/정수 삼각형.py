def triangle(n, triangle):
    m = len(triangle[-1])
    dp = [[0] * m for _ in range(n)]
    
    # initialize last row
    dp[-1] = triangle[-1]
    
    # iterate from second last to top
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    return dp[0][0]

n = int(input())
pyramid = []
for _ in range(n):
    floor = list(map(int, input().split()))
    pyramid.append(floor)

print(triangle(n, pyramid))