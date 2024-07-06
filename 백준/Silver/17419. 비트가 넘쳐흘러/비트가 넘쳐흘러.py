def smallbeat(k):
	count = 0
	while k != '0' * len(k):
		k_int = int(k, 2)
		k_int = k_int - (k_int & ((~k_int) + 1))
		k = format(k_int, '0' + str(len(k)) + 'b')
		count += 1
	return count

def largebeat(k):
	return k.count('1')

n = int(input())
k = str(input())

if n <= 30:
	print(smallbeat(k))
else:
	print(largebeat(k))