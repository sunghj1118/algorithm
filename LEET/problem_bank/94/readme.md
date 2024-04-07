# 94. Problem Review

## 94. Binary Tree Inorder Traversal

### Problem Definition
Given the root of a binary tree, return the inorder traversal of its nodes' values.

### Approach
- Create a DFS tree stack that traverses left, root, and right in that order.

### Solution

```python
# Url: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], [(root, False)]

        while stack:
            node, visited = stack.pop() # last element
            if node:
                if visited:
                    result.append(node.val)
                else: # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        
        return result
```