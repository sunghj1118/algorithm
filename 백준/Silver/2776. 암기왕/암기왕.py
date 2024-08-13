import bisect

def binary_search(note,q):
	i = bisect.bisect_left(note, q)
	if i != len(note) and note[i] == q:
		return 1
	else:
		return 0

t = int(input())

for _ in range(t):
	n = int(input())
	note = list(map(int, input().split()))
	m = int(input())
	questions = list(map(int, input().split()))

	note.sort()
	for q in questions:
		print(binary_search(note, q))