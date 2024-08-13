def ceiling_sqrt(n):
	lo, hi = 0, n
	result = 0

	while lo <= hi:
		mid = (lo+hi)//2

		if mid * mid == n:
			return mid
		elif mid * mid < n:
			lo = mid + 1
		else:
			result = mid
			hi = mid -1

	return result


n = int(input())
print(ceiling_sqrt(n))