def solve(stairs):
	# dp[i]는 i번째까지 최대 점수
	dp = [0] * 301

	# 초기값 설정
	dp[1] = stairs[1]
	dp[2] = stairs[1] + stairs[2]
	dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

	# 3번째부터 계산
	for i in range(4, n+1):
		dp[i] = max(dp[i-2] + stairs[i],  # 두 계단 전에서 현 계단으로
		dp[i-3] + stairs[i-1] + stairs[i]) # 세 계단 전에서 이전 계단 통했을 

	return dp[n]

n = int(input())
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

print(solve(stairs))