N,m = map(int, input().split())
lunches = []
for _ in range(m):
	lunches.append(int(input()))

lunches.sort()

count = 0
lunch_sum = 0
for l in lunches:
	lunch_sum += l
	if lunch_sum > N:
		break
	count += 1

print(count)