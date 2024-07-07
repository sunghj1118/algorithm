from collections import Counter

s = input().strip()

alphabet_counts = [0] * 26

count = Counter(s)

for char in count:
	if 'a' <= char <= 'z':
		alphabet_counts[ord(char) - ord('a')] = count[char]

print(' '.join(map(str, alphabet_counts)))