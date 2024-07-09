import math


def bridge_combinations(n, m):
	# dp[i][j]는 서쪽 i개, 동쪽 j개의 사이트로 다리를 놓는 경우의 수
	dp = [[0] * (m+1) for _ in range(n+1)]

	# 초기화: 서쪽 사이트가 0개일 때는 항상 1가지 경우 (다리를 짓지 않)
	for j in range(m+1):
		dp[0][j] = 1

	# 동적 계획법을 이용한 계산
	for i in range(1, n+1):
		for j in range(i, m+1):
			dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

	return dp[n][m]


t = int(input())

for _ in range(t):
	# 겹치지 않는 경우에 대해서 찾아야 하기 때문에, '이항계수' 사

	n, m = map(int, input().split())
	print(bridge_combinations(n, m))
