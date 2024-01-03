def count_ways(n):
    if n < 0:
        return 0

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

for _ in lst:
    print(count_ways(_))
