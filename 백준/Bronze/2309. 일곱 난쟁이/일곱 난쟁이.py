# find two dwarfs whose sum is equal to over
def find_dwarfs(li, over):
	for i in range(8):
		for j in range(i+1, 9):
			if li[i] + li[j] == over:
				li.pop(j)
				li.pop(i)
				return li


li = []
for _ in range(9):
	li.append(int(input()))

li.sort()
over = sum(li) - 100

li = find_dwarfs(li, over)
for i in range(7):
	print(li[i])