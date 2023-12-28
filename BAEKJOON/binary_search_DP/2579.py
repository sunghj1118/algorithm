N = int(input())
steps = []
dp = []

for _ in range(N):
    steps.append(int(input()))

dp.append(steps[0])
dp.append(max(steps[0]+steps[1],steps[1]))
dp.append(max(steps[0]+steps[1]),steps[1]+steps[2])
for i in range(3,N):
    dp.append(max(dp[i-2]+steps[i]),dp[i-3]+steps[i]+steps[i-1])

print(dp.pop())