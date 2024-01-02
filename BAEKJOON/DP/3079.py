# take inputs immigration N, people M
N, M = list(map(int,input().split()))

# take inputs of offices
times = []
for i in range(N):
    times.append(int(input()))
print(times)

left, right = min(times), max(times) * M
result = right

while left <= right:
    counter = 0
    mid = (left+right)//2

    for i in range(N):
        counter += mid //times[i]

    if counter >= M:
        right = mid -1
        result = min(mid, result)
    else:
        left = mid +1

print(result)