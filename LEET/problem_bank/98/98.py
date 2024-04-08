from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    i = 1

    while i < len(level_order):
        current = queue.pop(0)
        if level_order[i] is not None:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    return root




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


# Runner Code
root_list = [5,4,6,None,None,3,7]
root = build_tree(root_list)

# Expected: False
print(Solution().isValidBST(root))