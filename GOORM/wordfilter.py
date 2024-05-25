S, E = map(int, input().split())
Smess = input()
Emess = input()

while Smess in Emess:
	Emess = Emess.replace(Smess, "")

if len(Emess) == 0:
	print("EMPTY")
else:
	print(Emess)