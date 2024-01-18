def money(x):
    q = d = n = p = 0
    q = x//25
    x = x % 25
    d = x//10
    x = x % 10
    n = x//5
    p = x % 5

    print(q, d, n, p)


t = int(input())
for _ in range(t):
    money(int(input()))
