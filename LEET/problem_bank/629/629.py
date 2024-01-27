class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7  # MOD를 선언, 10^9 + 7로 초기화

        # DP 테이블을 만들고, 0으로 초기화
        dp = [[0] * (k+1) for _ in range(n+1)]

        # 0개의 역순쌍을 가지고 있는 크기 0과 크기 1의 수열은 1개이다.
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1

            # 1부터 k까지의 역순쌍을 가지고 있는 수열의 개수를 구한다.
            for j in range(1, k+1):
                # j개의 역순쌍을 가지고 있는 크기 i의 수열의 개수는 다음의 합과 같다:
                # - j개의 역순쌍을 가지고 있는 크기 i-1의 수열의 개수
                # - j-1개의 역순쌍을 가지고 있는 크기 i-1의 수열의 개수
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

                # j-i가 0보다 크거나 같은 경우, j개의 역순쌍을 가지고 있는 크기 i의 수열의 개수는 다음의 합과 같다:
                # - j-i개의 역순쌍을 가지고 있는 크기 i의 수열의 개수
                if j-i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i] + MOD) % MOD

        # n개의 원소를 가지고 있는 수열의 개수를 반환한다.
        return dp[n][k]


print(Solution().kInversePairs(3, 1))
