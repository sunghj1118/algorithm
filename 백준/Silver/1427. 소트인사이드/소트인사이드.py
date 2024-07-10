s = input()
li = list(s)
li.sort(reverse=True)
print("".join(map(str, li)))