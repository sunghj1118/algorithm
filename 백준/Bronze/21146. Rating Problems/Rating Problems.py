n, k = map(int, input().split())

total = 0
for i in range(k):
	total += int(input())

print(((total + (n-k)*(-3))/n), ((total + (n-k)*(3))/n))