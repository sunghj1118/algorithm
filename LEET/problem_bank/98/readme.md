# 98. Problem Review

## 98. Validate Binary Search Tree

### Problem Definition
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

### Approach
- Check if the current node is within the range of possible values by keeping track of a min and max val.

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursive(node, lower, upper):
            # Base case
            if not node:
                return True
            
            # Check if the current node is within the range
            if node.val <= lower or node.val >= upper:
                return False

            # Check the left and right subtree
            if not recursive(node.right, node.val, upper):
                return False

            if not recursive(node.left, lower, node.val):
                return False

            return True

        return recursive(root, float('-inf'), float('inf'))
```