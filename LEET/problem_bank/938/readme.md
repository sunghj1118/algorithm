# 938. Problem Review

## 938. Range Sum of BST

### Problem Definition
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

### Approach
- This is probably binary search

### Solution
- Solved with DFS.

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return current_val + left_sum + right_sum
        
        return dfs(root)
