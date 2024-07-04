n = int(input())
min_junk = 100000000000
date = 0
nums = list(map(int, input().split()))

for i in range(n):
    junk = nums[i]
    if junk < min_junk:
        min_junk = junk
        date = i

print(date)