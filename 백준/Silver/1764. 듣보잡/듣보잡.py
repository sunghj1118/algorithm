import sys

h, s = map(int, sys.stdin.readline().split())
heard = set()
heard_and_seen = []

for i in range(h):
	heard.add(sys.stdin.readline().strip())

for i in range(s):
	person = sys.stdin.readline().strip()
	if person in heard:
		heard_and_seen.append(person)

heard_and_seen.sort()

print(len(heard_and_seen))
for i in heard_and_seen:
	sys.stdout.write(i + '\n')