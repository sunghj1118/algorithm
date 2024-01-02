T = int(input())
values = []

for i in range(T):
    count0 = [1, 0]
    count1 = [0, 1]
    n = int(input())
    if n > 1:
        for i in range(n-1):
            count0.append(count1[-1])
            count1.append(count0[-2]+count1[-1])

    print(count0[n], count1[n])