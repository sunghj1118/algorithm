s = str(input())
jubmisa = [s]

while s:
    s = s[1:]
    jubmisa.append(s)

jubmisa = [value for value in jubmisa if value]

jubmisa.sort()

for value in jubmisa:
    print(value)
