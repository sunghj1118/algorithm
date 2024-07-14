n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True)

max_weight = 0

for i in range(n):
	max_weight = max(max_weight, ropes[i] * (i+1))
print(max_weight)