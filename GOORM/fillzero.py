n = int(input())
li = []

for i in range(n):
	data = list(map(int, input().split()))
	for j in range(len(data)):
		if data[j] == 0:
			zero_loc = i, j
		
	li.append(data)

	
x_sum = 0
y_sum = 0
for i in li[zero_loc[0]]:
	x_sum += i
for j in range(len(li)):
	y_sum += li[j][zero_loc[1]]
sum = x_sum+y_sum
print(sum)
