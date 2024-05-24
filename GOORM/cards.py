N, M = map(int, input().split())
li = set(range(1, N+1))
count = 0

for i in range(M):
	cur = int(input())
	count+=1
	if cur in li:
		li.remove(cur)
	if len(li) == 0:
		print(count)
		break

if len(li) > 0:
	print(-1)