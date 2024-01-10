# 2385. Problem Review

## 2385. Amount of Time for Binary Tree to Be Infected

### Problem Definition
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

### Approach
- Probably DFS.
- We also need to indicate whether or not the tree is infected.
- We also need a minute counter for every infection step.

### Solution
- GRAPH: Since a binary tree doesn't allow us to go up from child to parent, we need to convert the tree into a graph representation.
- BFS: Since we need to infect all nodes, bfs is better suited than dfs. We process level by level.
- Track infected nodes.
- Count mins

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def buildGraph(node, parent, graph):
            if not node:
                return
            if node.val not in graph:
                graph[node.val] = []
            if parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
                buildGraph(node.left, node, graph)
            if node.right:
                graph[node.val].append(node.right.val)
                buildGraph(node.right, node, graph)
            
        graph = {}
        buildGraph(root, None, graph)

        # BFS from start node
        minutes = 0
        queue = collections.deque([start])
        visited = set([start])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            if queue:
                minutes += 1
        return minutes
            
