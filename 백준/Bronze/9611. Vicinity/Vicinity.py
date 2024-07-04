from math import sqrt

# read the input
n = int(input())
points = []

for _ in range(n):
	x, y = map(int, input().split())
	points.append((x,y))

# for each test case find points in vicinity
t = int(input())

for _ in range(t):
	i, d = map(int, input().split())
	count = -1

	for point in points:
		x = point[0]-points[i-1][0]
		y = point[1]-points[i-1][1]
		distance = sqrt(x*x + y*y)
		if distance <= d:
			count += 1

	print(count)