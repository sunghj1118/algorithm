def count_sticks(X):
	# 이진수로 변환하여 1의 개수를 세는 방법
	return bin(X).count('1')

X = int(input())

print(count_sticks(X))