import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
queries = list(map(int,sys.stdin.readline().split()))

cards = set(cards)
results = []

for q in queries:
	if q in cards:
		results.append(1)
	else:
		results.append(0)

sys.stdout.write(' '.join(map(str, results)))
sys.stdout.write('\n')