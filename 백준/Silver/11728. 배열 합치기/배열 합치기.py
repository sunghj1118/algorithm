n, m = map(int,input().split())
li = []
a = list(map(int,input().split()))
b = list(map(int, input().split()))

a.extend(b)
a.sort()
result = ' '.join(str(x) for x in a)
print(result)