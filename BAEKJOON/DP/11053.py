#LIS: Longest Increasing Subsequence

def LIS(n, seq):
    dp = [1]*(n+1) # 원소들마다의 순서를 기록하는 dp 리스트
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]: # 현재 원소가 이전 원소보다 크다면
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


n = int(input()) # 수열의 길이
seq = list(map(int, input().split())) # 수열
print(LIS(n, seq))
