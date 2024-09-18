def max_substring_sum(n, arr):
    dp = [0] * n
    dp[0] = arr[0]
    max_sum = dp[0]
    
    for i in range(1, n):
        dp[i] = max(arr[i], arr[i]+dp[i-1])
        max_sum = max(max_sum, dp[i])
    
    return max_sum

n = int(input())
arr = list(map(int, input().split()))
print(max_substring_sum(n, arr))