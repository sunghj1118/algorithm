a, b, c = map(int, input().split())

def breakEven(a, b, c):
    count = 1
    point = -a - b + c
    if c <= b:
        return -1

    while point <= 0:
        point += -b + c
        count += 1

    return count

print(breakEven(a,b,c))