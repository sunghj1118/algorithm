import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
	x, y = map(int, sys.stdin.readline().split())
	li.append((x,y))

li.sort(key=lambda coord: (coord[1], coord[0]))
for x, y in li:
	sys.stdout.write(f"{x} {y}\n")