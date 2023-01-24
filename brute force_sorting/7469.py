N, M = [int(x) for x in input().split()]
a = list(map(int, input().split()))

def Q(i,j,k):
    current = a[i-1:j]
    current.sort()
    print(current[k-1])

for i in range(N):
    i, j, k = [int(x) for x in input().split()]
    Q(i,j,k)