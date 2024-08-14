def find_range(n, x):
    low, high = 0, n
    result = high
    while low <= high:
        mid = (low + high) // 2
        if is_sufficient(n, x, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def is_sufficient(n, lights, height):
    covered = 0
    for l in lights:
        start = max(0, l - height)
        end = min(n, l + height)
        if start <= covered:
            covered = max(covered, end)
        else:
            return False
        if covered >= n:
            return True
    return covered >= n

n = int(input())
m = int(input())  # num lights
x = list(map(int, input().split()))  # location lights

print(find_range(n, x))