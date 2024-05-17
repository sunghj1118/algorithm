# LIS: Longest Bitonic Subsequence

def LIS(n, seq):
    dp = [1]*(n+1) # 원소들마다 순서를 기록하는 dp 리스트
    dp2 = [1]*(n+1) # 원소들마다 역순서를 기록하는 dp 리스트

    # 순서대로 LIS
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]: # 현재 원소가 이전 원소들보다 크다면
                dp[i] = max(dp[i], dp[j]+1)
    
    # 역순 LIS
    for i in reversed(range(n)):
        for j in range(i, n):
            if seq[i] > seq[j]: # 현재 원소가 이전 원소들보다 크다면
                dp2[i] = max(dp2[i], dp2[j]+1)
    
    # 각각의 LIS dp 배열들을 합치기
    sum_dp = [1]*(n+1)
    for i in range(len(dp)):
        sum_dp[i] = dp[i] + dp2[i] -1
    
    # 최장 바이토닉 수열의 길이 반환
    return max(sum_dp)
            

n = int(input()) # 수열의 길이
seq = list(map(int, input().split())) # 수열
print(LIS(n, seq))