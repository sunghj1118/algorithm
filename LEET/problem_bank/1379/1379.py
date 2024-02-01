class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(ori, clo):
            # Root Node
            if ori:
                if ori == target:
                    self.ans = clo

                # Traverse left and right
                dfs(ori.left, clo.left)
                dfs(ori.right, clo.right)

        dfs(original, cloned)
        return self.ans


def list_to_tree(lst):
    def helper(index):
        if index < len(lst) and lst[index] is not None:
            node = TreeNode(lst[index])
            node.left = helper(2 * index + 1)
            node.right = helper(2 * index + 2)
            return node
        else:
            return None

    return helper(0)


def find_target(root, target_val):
    if root is None:
        return None
    if root.val == target_val:
        return root
    left = find_target(root.left, target_val)
    if left is not None:
        return left
    return find_target(root.right, target_val)


tree = list_to_tree([7, 4, 3, None, None, 6, 19])
cloned = list_to_tree([7, 4, 3, None, None, 6, 19])
target_val = 3
target = find_target(tree, target_val)

print(Solution().getTargetCopy(tree, cloned, target))
