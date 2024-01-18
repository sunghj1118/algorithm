def microwave(n):
    if n % 10 != 0:
        print(-1)
    else:
        a = b = c = 0
        a = n//300
        n = n % 300
        b = n//60
        n = n % 60
        c = n//10

        print(a, b, c)


(microwave(int(input())))
