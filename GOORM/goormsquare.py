n = int(input())
li = []

for i in range(n):
	start, end = input().split()
	li.append((int(start), int(end)))
	
# Sort events first by end times, then by start times
li = sorted(li, key=lambda x: (x[1], x[0]))

count = 0

# Count possible events by checking if the start time of the next time is larger or equal to 1. 
cur_time = li[0]
for i in range(len(li)):
	if (li[i][0] - cur_time[1]) > 0:
		count += 1
		cur_time = li[i]
	
print(count+1)