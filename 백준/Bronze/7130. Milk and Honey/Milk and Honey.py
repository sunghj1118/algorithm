m, h = map(int, input().split())
n = int(input())
total = 0
for _ in range(n):
	c, b = map(int, input().split())
	total += max(c*m, b*h)

print(total)