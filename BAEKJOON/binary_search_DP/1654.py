

K, N = list(map(int, input().split()))
cables = []

for og in range(K):
    cables.append(int(input()))
start, end = 1, max(cables)

while start <= end:
    mid = (start+end)//2
    ncables = 0
    for i in cables:
        ncables += i // mid
    
    if ncables >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)