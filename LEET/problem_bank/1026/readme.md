# 1026. Problem Review

## 1026. Maximum Difference Between Node and Ancestor

### Problem Definition
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

### Approach
- Search the entire tree until no nodes left.
- Calculate differences.
- Since we're looking at ancestors, it will probably be DFS.
- Since we're finding the greatest diff, we don't need to store all ancestors, only the largest one and smallest one.


### Solution
- DFS(node, min, max)
- compare the current min with the current node.
- compare the current max with the current node.
- compare the left diff and the right diff.

```python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)

            left = dfs(node.left, cur_min, cur_max)
            right = dfs(node.right, cur_min, cur_max)
            return max(left, right)
        return dfs(root, root.val, root.val)
