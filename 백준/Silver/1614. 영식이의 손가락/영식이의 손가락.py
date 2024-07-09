injured_finger = int(input())
durability = int(input())

def count_max(injured, durability):
	fingers = [1,2,3,4,5,4,3,2]
	cycle_length = 8
	injured_count_per_cycle = fingers.count(injured_finger)

	if injured_count_per_cycle == 0:
		return durability * cycle_length

	full_cycles = durability // injured_count_per_cycle
	remaining = durability % injured_count_per_cycle

	count = full_cycles * cycle_length

	for i in range(cycle_length):
		if fingers[i] == injured_finger:
			remaining -= 1
			if remaining == -1:
				break
		count += 1

	return count


print(count_max(injured_finger, durability))