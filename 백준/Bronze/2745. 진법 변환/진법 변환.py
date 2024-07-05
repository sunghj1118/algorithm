def to_decimal(n, b):
	decimal = 0
	power = 0

	# 문자열을 뒤집어서 낮은 자리수부터 처리
	for digit in reversed(n):
		# 알파벳인 경우 숫자로 변환
		if digit.isalpha():
			value = ord(digit) - ord('A') + 10
		else:
			value = int(digit)

		# 해당 자리의 값을 계산하여 더함
		decimal += value * (b ** power)
		power += 1

	return decimal


n, b = map(str, input().split())
b = int(b)

result = to_decimal(n, b)
print(result)