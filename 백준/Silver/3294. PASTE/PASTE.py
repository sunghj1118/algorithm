def cutandpaste(n,k,ops):
	document = list(range(1,n+1))

	for a,b,c in ops:
		a,b,c = a-1,b-1,c

		cutsection = document[a:b+1]
		del document[a:b+1]

		if c==0:
			document = cutsection + document
		else:
			document = document[:c] + cutsection + document[c:]

	return document[:10]

n, k = map(int, input().split())
ops = [[0,0,0]] * k
for i in range(k):
	a,b,c = map(int, input().split())
	ops[i] = [a,b,c]

result = cutandpaste(n,k,ops)
for num in result:
	print(num)