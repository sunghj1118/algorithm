def edit(rules, line):
	for a, b in rules:
		while a in line:
			line = line.replace(a, b, 1)

	return line

while True:
	n_rules = int(input())

	if n_rules == 0:
		break

	rules = [0] * n_rules
	for i in range(n_rules):
		find = str(input())
		after = str(input())
		rules[i] = (find, after)

	line = str(input())

	print(edit(rules, line))