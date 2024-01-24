# 1457. Problem Review

## 1457. Pseudo-Palindromic Paths in a Binary Tree

### Problem Definition
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

### Approach
- DFS. 
    - init a counter of pseudo-palindromic paths
    - start a dfs from the root. pass along a path counter that keeps track of the count of each digit
    - for each node visited, increase count
    - if the node is a leaf (no children), check if the path counter is a pseudo-palindrome.
        - if is a P-P if at most one of the counts is odd.
        - if it is PP, increment the pp paths counter.
    - continue the dfs to the left and right children, passing the updated path counter.
    - after visiting node, decrement the count of its value to backtrack.
    - once the DFS is complete, the counter will hold the number of PP.


### Solution

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        path = [0] * 10  # 0 ~ 9

        def dfs(node):
            if node:
                # increment path count corresponding to the value of the node
                path[node.val] += 1

                # if it's a leaf check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    if sum(v % 2 for v in path) < 2:
                        self.count += 1

                # traverse left and right
                dfs(node.left)
                dfs(node.right)

                # decrement path count after backtracking
                path[node.val] -= 1

        dfs(root)
        return self.count
