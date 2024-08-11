n,b = map(int, input().split())
gifts = []
for i in range(n):
	p,s = map(int, input().split())
	gifts.append((p,s,p+s))

gifts.sort(key=lambda x: x[2])

# max gifts without token use
max_gifts = 0
current_budget = b

for p,s,total in gifts:
	if current_budget >= total:
		current_budget -= total
		max_gifts += 1
	else:
		break

# try using token on each gift to see if it increases the count
for i in range(n):
	# calculate the cost with the coupon
	coupon_cost = gifts[i][0]//2 +gifts[i][1]

	if coupon_cost <= b:
		remaining_budget = b - coupon_cost
		count_with_coupon = 1

		for j in range(n):
			if j != i and remaining_budget >= gifts[j][2]:
				remaining_budget -= gifts[j][2]
				count_with_coupon += 1
		max_gifts = max(max_gifts, count_with_coupon)

print(max_gifts)