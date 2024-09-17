def cheapest_color(n, prices):
	# initialize dp
	dp = [[0,0,0] for i in range(n)]

	# initialize base case
	dp[0] = prices[0]

	# fill table
	for i in range(1, n):
		# 0:red
		dp[i][0] = prices[i][0] + min(dp[i-1][1], dp[i-1][2])

		# 1:green
		dp[i][1] = prices[i][1] + min(dp[i-1][0], dp[i-1][2])

		# 2:blue
		dp[i][2] = prices[i][2] + min(dp[i-1][0], dp[i-1][1])

	return min(dp[n-1])

n = int(input())
prices = []
for _ in range(n):
	RGB = list(map(int, input().split()))
	prices.append(RGB)

print(cheapest_color(n, prices))