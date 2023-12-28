N = int(input())
people = []
weights = []


for i in range(0, N):
    current = list(map(int, input().split()))
    people.append(current)


for i in people:
    counter = 1
    for j in people:
        if(i[0] < j[0] and i[1] < j[1]):
            counter += 1
    weights.append(counter)

for i in range(N):
    print(weights[i], end=" ")