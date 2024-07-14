from heapq import heappop, heappush
import sys

def max_value(gems, bags):
	"""
	When given two lists:
	- gems: provides gem weight M, and price V
	- bags: provides possible weight capacity C
	Find out max possible value possible to carry.
	"""
	gems.sort(key=lambda x: (x[0]))
	bags.sort()
	
	total_price = 0
	gem_index = 0
	heap = []

	for bag in bags:
		while gem_index < len(gems) and gems[gem_index][0] <= bag:
			heappush(heap, -gems[gem_index][1])
			gem_index += 1
		
		if heap:
			total_price -= heappop(heap)

	return total_price



n, k = map(int, sys.stdin.readline().split())
gems = []
bags = []
for i in range(n):
	m, v = map(int, sys.stdin.readline().split())
	gems.append((m,v))

for i in range(k):
	c = int(sys.stdin.readline())
	bags.append(c)

result = max_value(gems, bags)
print(result)