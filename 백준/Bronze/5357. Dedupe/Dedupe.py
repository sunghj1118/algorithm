n = int(input())

for i in range(n):
	s = input()
	out = s[0]

	for j in range(1,len(s)):
		if s[j] != s[j-1]:
			out += s[j]

	print(out)