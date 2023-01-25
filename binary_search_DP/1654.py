K, N = list(map(int, input().split()))
cables = []

for i in range(K):
    cables[i] = int(input(N))
cables.sort()

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high+low)//2
        
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            return binary_search(arr, low, mid -1, x)
        else:
            return binary_search(arr, mid +1, high, x)
    else:
        return 0


for i in range(0, M):
    print(binary_search(cables, 1, cables[-1], x))
