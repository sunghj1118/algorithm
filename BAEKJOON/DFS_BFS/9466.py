#recursion error handling
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(x):
    global ans
    visit[x] = True
    cycle.append(x)
    num = selections[x]

    if visit[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

T = int(input())

for _ in range(T):
    n = int(input())
    selections = [0] + list(map(int, input().split()))
    visit = [False] * (n+1)
    ans = []

    for i in range(1, n+1):
        if not visit[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))