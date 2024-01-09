# 872. Problem Review

## 872. Leaf-Similar Trees

### Problem Definition
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

### Approach
- This is probably DFS with a binary tree approach just like `938. Range Sum of BST`.

### Solution
- Define a def DFS.
- If the node is empty, return empty list [].
- If the node is a leaf, return the node value.
- Else, return the dfs(left node) + dfs(right node)

- Compare the two trees

```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:  # leaf node
                return [node.val]
            return dfs(node.left) + dfs(node.right)

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        # Compare the two lists
        return leaves1 == leaves2
