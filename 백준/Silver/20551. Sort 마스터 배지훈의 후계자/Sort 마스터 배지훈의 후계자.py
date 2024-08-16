from bisect import bisect_left

def binary_search(question, arr):
	idx = bisect_left(arr, question)
	if idx != len(arr) and arr[idx] == question:
		return idx
	return -1


n, m = map(int, input().split()) # elements n, queries m
a = [int(input()) for _ in range(n)]
a.sort()

for i in range(m):
	print(binary_search(int(input()), a))