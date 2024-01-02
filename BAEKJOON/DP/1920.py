N = int(input())
ourlist = list(map(int, input().split()))
ourlist.sort()
M = int(input())
list_to_check = list(map(int, input().split()))

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
    print(binary_search(ourlist, 0, len(ourlist)-1, list_to_check[i]))
