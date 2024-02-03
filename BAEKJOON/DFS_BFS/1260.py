from collections import deque
import sys
read = sys.stdin.readline


def bfs(v):
    # Initialize a queue with the starting node
    q = deque()
    q.append(v)

    # Mark the starting node as visited
    listBFS[v] = 1

    # While there are nodes in the queue
    while q:
        # Remove the first node from the queue
        v = q.popleft()

        # Print the current node
        print(v, end=" ")

        # Iterate over all nodes
        for i in range(1, n+1):
            # If the node at index i has not been visited and there is an edge between the current node and node i
            if listBFS[i] == 0 and graph[v][i] == 1:
                # Add node i to the queue
                q.append(i)

                # Mark node i as visited
                listBFS[i] = 1


def dfs(v):
    # Mark the current node as visited
    listDFS[v] = 1

    # Print the current node
    print(v, end=" ")

    # Iterate over all the nodes
    for i in range(n+1):
        # If the node at index i has not been visited and there is an edge between the current node and node i
        if listDFS[i] == 0 and graph[v][i] == 1:
            # Recursively call the DFS function node i
            dfs(i)


# Read the number of nodes, edges, and the start node
n, m, v = map(int, read().split())

# Initialize the adjacency matrix with 0s
graph = [[0] * (n+1) for _ in range(n+1)]

# Initialize the visit lists for BFS and DFS
listBFS = [0] * (n+1)
listDFS = [0] * (n+1)

# Read the edges
for _ in range(m):
    a, b = map(int, read().split())
    # Add the edge to the adjacency matrix
    graph[a][b] = graph[b][a] = 1

# Perform DFS starting from node v
dfs(v)
print()

# Perform BFS starting for node v
bfs(v)
