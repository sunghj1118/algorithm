import sys

t = int(sys.stdin.readline())
for i in range(t):
	n = int(sys.stdin.readline())
	candidates = []
	for j in range(n):
		document, interview = map(int, input().split())
		candidates.append((document, interview))
		
	candidates.sort() # sort by document score

	competent = 0
	min_interview_score = float('inf')
	# check if there is a candidate who is more competent in both areas
	for _, interview_rank in candidates:
		if interview_rank < min_interview_score:
			competent += 1
			min_interview_score = interview_rank

	print(competent)