# summer N, time for harvest T, containers C, price P
n, t, c, p = map(int, input().split())

print((n-1)//t * c * p)