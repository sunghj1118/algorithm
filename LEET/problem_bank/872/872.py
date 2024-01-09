class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:  # leaf node
                return [node.val]
            # traverse left subtree, then right subtree
            return dfs(node.left) + dfs(node.right)

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        # Compare the two lists
        return leaves1 == leaves2
