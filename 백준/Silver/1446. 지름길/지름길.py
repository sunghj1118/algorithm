import sys

def dp(n, d, shortcuts):
    dp = [sys.maxsize] * (d+1)
    dp[0] = 0

    shortcuts.sort(key=lambda x:x[1])

    for i in range(d+1):
        # update if reachable with shorter path
        if i > 0:
            dp[i] = min(dp[i], dp[i-1] +1)
        
        # check if any shortcut ends at this position
        for start, end, length in shortcuts:
            if end == i:
                dp[i] = min(dp[i], dp[start] + length)

    return dp[d]

n, d = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(n)]
result = dp(n, d, shortcuts)
print(result)