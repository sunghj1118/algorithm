n = int(input())
count = 0 # ways to represent N
start = 1 # possible starting number

# iterate until the sum of series up to 'start' exceeds N
while start * (start+1) //2 <= n:
	# calculate diff between N and sum of series
	# using formula: n - (start * (start+2) // 2)
	diff = n - (start * (start + 1) // 2)

	# check if the diff is divisible by 'start'
	# if it is, this is a valid way to represent N
	if diff % start == 0:
		count += 1

	# move to the next possible starting num
	start += 1

# print final count of ways to represent N
print(count)