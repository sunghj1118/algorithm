numcities = int(input())

distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

total = distances[0] * cities[0]
current = cities[0]

for i in range(1, numcities -1):
    if(current < cities[i]):
        total += current * distances[i]
    else:
        current = cities[i]
        total += current * distances[i]

print(total)