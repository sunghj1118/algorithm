import sys

def min_diff_values(nums):
	"""
	Find pair of values that provide min difference
	"""

	nums.sort()
	closest_sum = float('inf')
	left = 0
	right = len(nums) -1
	closest_pair = None

	while left < right:
		current_sum = nums[left] + nums[right]

		# update if closer to 0
		if abs(current_sum) < abs(closest_sum):
			closest_sum = current_sum
			closest_pair = (nums[left], nums[right])

		# move pointers based on sum
		if current_sum < 0:
			left += 1
		elif current_sum > 0:
			right -= 1
		else:
			return (nums[left], nums[right])
	
	return closest_pair


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

pair = min_diff_values(nums)
print(pair[0], pair[1])