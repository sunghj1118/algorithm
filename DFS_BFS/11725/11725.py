# set recursion limit higher
import sys
sys.setrecursionlimit(10**6)

# get input

# line 1: amount of nodes
N = int(input())

tree = [[] for _ in range(N + 1)]

# line 2~N: node info
for _ in range(N - 1):
    parent, child = map(int, input().split())
    tree[parent].append(child)
    tree[child].append(parent)

# DFS
# initialize parent array
parent = [0 for _ in range(N + 1)]


def dfs():
    # start from node 1
    stack = [1]

    # while the stack is not empty; while there are nodes to visit
    while stack:
        current_node = stack.pop()
        for child in tree[current_node]:
            # if the child is not the parent of the current node, set the current node as the parent of the child
            if child != parent[current_node]:
                parent[child] = current_node
                stack.append(child)


# DFS starts from node 1
dfs()

# Print the parent of each node from node 2 to N
for i in range(2, N + 1):
    print(parent[i])
