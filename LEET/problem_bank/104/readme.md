# 104. Problem Review

## 104. Symmetric Tree

### Problem Definition
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Approach
- If both trees are empty (or end), they are the same.
- If one of the trees is empty, they are not the same.
- If the values of the nodes are different, they are not the same.
- Keep passing the depth of the left and right subtrees until the end of the tree.

### Solution

```python
# Url: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        # No root, return 0
        if not root:
            return 0
        
        # Recursive function to find the depth of the tree
        def find_depth(left: Optional[TreeNode], right: Optional[TreeNode], depth) -> int:
            if not left and not right:
                return depth
            elif not left:
                return find_depth(right.left, right.right, depth + 1)
            elif not right:
                return find_depth(left.left, left.right, depth + 1)
            else:
                return max(find_depth(left.left, left.right, depth + 1), find_depth(right.left, right.right, depth + 1))
        
        return find_depth(root.left, root.right, depth)
```