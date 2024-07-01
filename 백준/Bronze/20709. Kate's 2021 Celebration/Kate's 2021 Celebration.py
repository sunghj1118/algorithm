n = int(input())

def has2021(digits):
	required_digits = {'2': 2, '0': 1, '1': 1}
	digits = str(digits)
	for digit in digits:
		if digit in required_digits:
			required_digits[digit] -= 1
			if all(count <= 0 for count in required_digits.values()):
				return True
	return False


possible_packs = []
for i in range(n):
	price, digits = map(str, input().split())
	price = int(price)

	# find if '2', '0', '2', '1' in digits
	# maybe use a dictionary?
	# what is the fastest and most efficient way to check
	# given digits = something like 9123480123984

	# append to a list only if the pack has 2021
	if has2021(digits):
		possible_packs.append((i+1, price))

# print the index 0 of the tuple based on the minimum price possible (index 1)
if possible_packs == []:
	print(0)
else:
	min_value = min(possible_packs, key=lambda x: x[1])
	print(min_value[0])