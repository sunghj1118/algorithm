# 100. Problem Review

## 100. Same Tree

### Problem Definition
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Approach
- If both trees are empty (or end), they are the same.
- If one of the trees is empty, they are not the same.
- If the values of the nodes are different, they are not the same.
- Recursively check the left and right subtrees.

### Solution

```python
# Url: https://leetcode.com/problems/same-tree/submissions/1227192284/

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case: If both nodes are None, return True
        if not p and not q:
            return True
        
        # If one of the nodes is None, return False
        if not p or not q:
            return False
        # If the node values are different, return False
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```