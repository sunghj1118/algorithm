N = int(input())
M = 0

for i in range(1, N+1):
    current = list(map(int, str(i)))
    sum_curr = i + sum(current)
    if(sum_curr == N):
        M = i
        break

print(M)