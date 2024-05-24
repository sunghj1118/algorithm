n = int(input())
count = 1

for i in range(n):
	for j in range(n):
		print(count, end="")
		if j == (n-1):
			print("\n", end="")
		else:
			print(" ", end="")
		count+=1