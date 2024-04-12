# 101. Problem Review

## 101. Symmetric Tree

### Problem Definition
https://leetcode.com/problems/symmetric-tree/submissions/1230064112/

### Approach
- If both trees are empty (or end), they are the same.
- If one of the trees is empty, they are not the same.
- If the values of the nodes are different, they are not the same.
- If the value of the nodes are the same, and the left subtree of the left tree is the same as the right subtree of the right tree, and the right subtree of the left tree is the same as the left subtree of the right tree, they are the same.

### Solution

```python
# Url: https://leetcode.com/problems/symmetric-tree/submissions/1230064112/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left):
                return True
            return False
        
        return is_mirror(root.left, root.right)
```