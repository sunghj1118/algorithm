import math
import sys

for line in sys.stdin:
	R, S = map(float, line.split())
	V = math.sqrt((R*(S+0.16))/0.067)
	print(round(V))