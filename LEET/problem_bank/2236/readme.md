# 2236. Problem Review

## 2236. Root Equals Sum of Children

### Problem Definition
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

Example 1:

    Input: root = [10,4,6]
    Output: true
    Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
    10 is equal to 4 + 6, so we return true.

Example 2:

    Input: root = [5,3,1]
    Output: false
    Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
    5 is not equal to 3 + 1, so we return false.
 

Constraints:

    The tree consists only of the root, its left child, and its right child.
    -100 <= Node.val <= 100

### Approach
- I will need to add the left node and the right node and compare that with the root node.
- Plan for constraints in the case where the node value is out of bounds.

### Solution
- Check for constraints and then check whether the sum is equal to the root node.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        if (root.val >= -100 or root.val <= 100):
            if ((root.left.val + root.right.val) == root.val):
                return True
            else:
                return False
        else:
            return False
