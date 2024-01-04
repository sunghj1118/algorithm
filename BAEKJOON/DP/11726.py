def tiling(n):
    """
    백준11726: 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 문제
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):  # 3부터 n까지
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 10007


n = int(input())
print(tiling(n))
