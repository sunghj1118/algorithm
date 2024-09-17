def mood(n,curr,percents):
	GG, GB, BG, BB = percents

	# dp array
	dp = [[0,0] for _ in range(n+1)]

	# initial mood
	dp[0][curr] = 1

	# probabilities for each day
	for i in range(1, n+1):
		dp[i][0] = dp[i-1][0] * GG + dp[i-1][1] * BG
		dp[i][1] = dp[i-1][0] * GB + dp[i-1][1] * BB

	# probabilities for day N
	good_prob = round(dp[n][0] * 1000)
	bad_prob = round(dp[n][1] * 1000)

	return good_prob,bad_prob

n,curr = map(int, input().split())
percents = list(map(float, input().split()))

good_prob, bad_prob = mood(n,curr,percents)
print(good_prob)
print(bad_prob)