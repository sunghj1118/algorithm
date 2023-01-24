N, M = [int(x) for x in input().split()]
people = []
weights = []
rolls = list(map(int, input().split()))
possible = 0

for i in range(N):
    while(rolls[i] >= 10):
        if(rolls[i] == 10):
            possible += 1
            rolls[i] = rolls[i] - 10
        elif(rolls[i] > 10 and M > 0):
            M -= 1
            possible += 1
            rolls[i] = rolls[i] - 10


print(possible)