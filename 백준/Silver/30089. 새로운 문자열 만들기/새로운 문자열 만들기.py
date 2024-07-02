def longest_palindromic_substr(s):
	for i in range(len(s)):
		if s[i:] == s[i:][::-1]:
			if i == 0:
				break
			s += s[i-1::-1]
			break
	return s

t = int(input())
for _ in range(t):
	s = input()
	print(longest_palindromic_substr(s))