def find_fraction(X):
	diagonal = 1
	sum_prev_diagonals = 0

	# Find the diagonal number
	while sum_prev_diagonals + diagonal < X:
		sum_prev_diagonals += diagonal
		diagonal += 1

	# Find position in the diagonal
	position = X - sum_prev_diagonals

	# Determine numerator and denominator
	if diagonal % 2 == 0:
		numerator = position
		denominator = diagonal - position + 1
	else:
		numerator = diagonal - position + 1
		denominator = position

	return f"{numerator}/{denominator}"

X = int(input())

print(find_fraction(X))