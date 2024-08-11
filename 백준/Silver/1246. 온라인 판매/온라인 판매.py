n,m = map(int, input().split())
p = [0] * m
for i in range(m):
	p[i] = int(input())

p.sort()

total = []
max_p, tot_p = 0, 0
for i in range(m):
	eggs = min(n, m-i)
	curr = p[i]*(eggs)
	total.append(curr)
	if curr > tot_p:
		tot_p = curr
		max_p = p[i]

print(max_p, tot_p)