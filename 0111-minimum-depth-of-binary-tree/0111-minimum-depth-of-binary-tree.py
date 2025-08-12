# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        min_depth = float('inf')
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if node:
                if not node.left and not node.right:
                    min_depth = min(min_depth, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        
        return min_depth