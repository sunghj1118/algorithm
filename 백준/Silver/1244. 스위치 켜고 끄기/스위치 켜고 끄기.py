def flip_switch(sex, switch, switches):
	# MALE
	if sex == 1:
		# switch all factors of the switch
		for s in range(len(switches)):
			if (s+1) % switch == 0:
				switches[s] = 1 - switches[s]
	# FEMALE
	else:
		# find range
		# check parity on both sides of the switch
		# switch all switches that are mirrored
		switch -= 1
		lo = switch
		hi = switch
		while lo > 0 and hi < len(switches)-1:
			if switches[lo-1] == switches[hi+1]:
				lo -= 1
				hi += 1
			else:
				break

		for i in range(lo, hi+1):
			switches[i] = 1 - switches[i]

	return switches


n = int(input())
switches = list(map(int, input().split()))
num_students = int(input())
for i in range(num_students):
	sex, switch = (map(int, input().split()))
	switches = flip_switch(sex, switch, switches)

for i in range(0, len(switches), 20):
    print(' '.join(map(str, switches[i:i+20])))