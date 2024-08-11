def score(tests):
    tests.sort()
    tests.pop(0)
    tests.pop()
    if tests[-1] - tests[0] >= 4:
        return 'KIN'
    else:
        return sum(tests)

t = int(input())
tests = []
for _ in range(t):
    print(score(list(map(int, input().split()))))