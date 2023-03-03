N = int(input())
weights = list(map(int, input().split()))

sum = 0
current = 0


for i in range(0, len(weights)):
    sum = sum + weights[i]
    if weights[i] <= sum + 1:
        if i == 0:
            sum = sum + 1
        else:
            sum = sum - weights[i] + 1
        break

print(sum)