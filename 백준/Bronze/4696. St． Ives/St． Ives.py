while True:
	n = float(input())

	if n == 0:
		break
	
	result = n*n*n*n + n*n*n + n*n + n + 1
	print(f"{result:.2f}")