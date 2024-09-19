def max_bag(n, k, items):
    # initialize
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # fill table
    for i in range(1, n+1):
        for w in range(1, k+1):
            weight, value = items[i-1]
            if weight <= w:
                # include this item or not
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                # item is too heavy
                dp[i][w] = dp[i-1][w]

    return dp[n][k]

n, k = map(int, input().split())
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))

print(max_bag(n,k,items))