import sys

N = int(sys.stdin.readline())

counts = [0] * 10001

for _ in range(N):
    number = int(input())
    counts[number] += 1

counts.sort()

for value in range(10001):
    if counts[value] != 0:
        for _ in range(counts[value]):
            print(value)
