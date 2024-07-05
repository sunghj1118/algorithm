m = int(input())
n = int(input())

# prime numbers: divisible by only itself and 1
# how to find?
def is_prime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False

	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

summ = 0
min_value = 0
for i in range(m, n+1):
	# check if prime
	if is_prime(i):
		# if min_value not set yet
		if not min_value:
			min_value = i

		summ += i

if not summ:
	print(-1)
else:
	print(summ)
	print(min_value)