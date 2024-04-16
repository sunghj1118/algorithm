from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
        

# Test [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth(root))  # Expected: 3
