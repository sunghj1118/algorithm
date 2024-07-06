n = int(input())
k = str(input())

def dropthebeat(k):
	k_int = int(k, 2)
	result_int =  k_int-(k_int&((~k_int)+1))
	return format(result_int, '0' + str(len(k)) + 'b')

count = 0
while k != '0' * len(k):
	k = dropthebeat(k)
	count += 1

print(count)