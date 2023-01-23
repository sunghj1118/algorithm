count = 0

while(True):
    L, P, V = map(int, input().split())

    if(L == P == V == 0):
        break

    days = (V // P) * L
    left_days = V % P
    if(left_days > L):
        days += L
    else:
        days += left_days

    count += 1
    print("Case %d: %d" %(count, days))