count = 0
steps = []


def towerOfHanoi(n, from_rod, to_rod, aux_rod):  # n = current_num_of_disk
    global count
    if n == 0:
        return
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    count += 1
    steps.append(str(from_rod) + " " + str(to_rod))
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)


N = int(input())

towerOfHanoi(N, 1, 3, 2)
print(count)
for step in steps:
    print(step)
