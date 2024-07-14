def larger_than_x(n, li, x):
	"""
	Need to find unique pair of numbers n in li that are larger than x.
	"""

	li.sort()
	count = 0
	left = 0
	right = n -1

	while left < right:
		current_sum = li[left] + li[right]
		if current_sum == x:
			count += 1
			left += 1
			right -= 1
		elif current_sum < x:
			left += 1
		else:
			right -= 1

	return count

n = int(input())
li = list(map(int, input().split()))
x = int(input())

result = larger_than_x(n, li, x)
print(result)