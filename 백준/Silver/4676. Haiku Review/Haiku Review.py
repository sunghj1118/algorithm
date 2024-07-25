def is_haiku(haiku):
	def count_syllables(line):
		vowels = 'aeiouy'
		prev_char = " "
		count = 0
		for char in line:
			# if there is a vowel and the next character is not a vowel
			if char in vowels and prev_char not in vowels:
				count += 1
			prev_char = char

		return count

	# line 1
	# check if there are 5 syllables
	if count_syllables(haiku[0]) != 5:
		return 1
	# line 2
	if count_syllables(haiku[1]) != 7:
		return 2
	# line 3
	if count_syllables(haiku[2]) != 5:
		return 3

	return 'Y'

while True:
	haiku = list(input().split("/"))

	if haiku == ['e','o','i']:
		break

	print(is_haiku(haiku))