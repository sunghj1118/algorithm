import sys
from itertools import combinations

def dfs(start, group, visited):
    stack = [start]
    visited[start] = True
    count = 1
    total = population[start]

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor] and neighbor in group:
                stack.append(neighbor)
                visited[neighbor] = True
                count += 1
                total += population[neighbor]
    
    return count, total

def is_connected(group):
    visited = [False] * (n+1)
    start = next(iter(group))
    count, total = dfs(start, group, visited)
    return count == len(group), total

def solve():
    min_diff = float('inf')

    for i in range(1, n // 2 + 1):
        for combo in combinations(range(1, n+1), i):
            group1 = frozenset(combo)
            group2 = frozenset(range(1, n+1)) - group1

            connected1, total1 = is_connected(group1)
            if not connected1:
                continue
                
            connected2, total2 = is_connected(group2)
            if not connected2:
                continue
                
            diff = abs(total1 - total2)
            min_diff = min(min_diff, diff)
        
    
    return min_diff if min_diff != float('inf') else -1

n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    adjacent = list(map(int, input().split()))
    graph[i] = adjacent[1:]

result = solve()
print(result)