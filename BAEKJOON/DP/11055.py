# LIS: Sum of Longest Increasing Sequence
# 기본 LIS 알고리즘
def sumLIS(n, seq):
    dp = [0] * (n+1)
    sum_dp = seq[:] # 합에 대한 수열 생성
    
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                # 현재 값과 새로운 합 중 큰걸로 갱신
                sum_dp[i] = max(sum_dp[i], sum_dp[j]+seq[i]) 
    return max(sum_dp) # 최대값 반환
    

n = int(input())
seq = list(map(int, input().split()))
print(sumLIS(n, seq))