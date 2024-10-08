from collections import defaultdict

def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def solve(n, comparisons):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for a,b in comparisons:
        graph[a].append(b)
        reverse_graph[b].append(a)
    
    results = []
    for i in range(1, n+1):
        # find lighter items
        lighter = set()
        dfs(graph, i, lighter)

        # find heavier items
        heavier = set()
        dfs(reverse_graph, i, heavier)

        # count unknown relationships
        unknown = n - len(lighter | heavier)
        results.append(unknown)

    return results

n = int(input())
m = int(input())
comparisons = [tuple(map(int, input().split())) for _ in range(m)]

for result in solve(n, comparisons):
    print(result)