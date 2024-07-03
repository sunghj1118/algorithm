a, b, c = map(int, input().split())

# add
if a+b == c:
    print(str(a) + "+" + str(b) + "=" + str(c))
elif a == b+c:
    print(str(a) + "=" + str(b) + "+" + str(c))
# subtract
elif a-b == c:
    print(str(a) + "-" + str(b) + "=" + str(c))
elif a == b-c:
    print(str(a) + "=" + str(b) + "-" + str(c))
# multiply
elif a*b == c:
    print(str(a) + "*" + str(b) + "=" + str(c))
elif a == b*c:
    print(str(a) + "=" + str(b) + "*" + str(c))
# divide
elif a/b == c:
    print(str(a) + "/" + str(b) + "=" + str(c))
elif a == b/c:
    print(str(a) + "=" + str(b) + "/" + str(c))