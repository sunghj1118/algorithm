kda = str(input())
k, d, a = map(int,kda.split('/'))
if k+a < d or d == 0:
	print('hasu')
else:
	print('gosu')