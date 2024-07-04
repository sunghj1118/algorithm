def selectionSort(A, B):
	n = len(A)
	if A == B:
		return 1

	for last in range(n-1, 0, -1):
		max_index = 0
		for i in range(1, last+1):
			if A[i] > A[max_index]:
				max_index = i
		if last != max_index:
			A[last], A[max_index] = A[max_index], A[last]
			if A == B:
				return 1
	return 0

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(selectionSort(A, B))