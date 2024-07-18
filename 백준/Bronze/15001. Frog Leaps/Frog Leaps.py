import sys

input = sys.stdin.readline

n = int(input())

ans = 0
old = int(input())

for _ in range(n-1):
	x = int(input())
	ans += (x-old) ** 2
	old = x

print(ans)