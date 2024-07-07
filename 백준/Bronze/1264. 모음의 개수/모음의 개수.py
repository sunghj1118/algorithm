while True:
	line = input().lower()
	if line == '#':
		break

	count = 0
	vowels = ['a', 'e', 'i', 'o', 'u']
	for c in line:
		if c in vowels:
			count += 1

	print(count)