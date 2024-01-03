def min_ops_to_1(N):
    dp = [0] * (N + 1)
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어질 때, 2로 나누는 연산
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[N]


# 예시 사용
N = int(input())
print(min_ops_to_1(N))  # 10을 1로 만드는데 필요한 최소 연산 횟수
