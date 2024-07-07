n, m = map(int, input().split())
li = []
for i in range(n):
	line = str(input())
	li.append(line)

for i in li:
	print(i[::-1])