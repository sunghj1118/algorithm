import sys

while True:
	line = sys.stdin.readline().strip()

	if line == 'END':
		break
	
	reversed_line = line[::-1]

	print(reversed_line)