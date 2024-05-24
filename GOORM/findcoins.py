def find_coins(n):
	count = 0
	if n >= 40:
		count = n // 40
		n = n % 40
	if n >= 20:
		count = count + n // 20
		n = n % 20
	if n >= 10:
		count = count + n // 10
		n = n % 10
	if n >= 5:
		count = count + n // 5
		n = n % 5
	if n >= 1:
		count = count + n // 1
		n = n % 1
	print(count)

n = int(input())
find_coins(n)
