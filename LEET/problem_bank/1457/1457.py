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


def list_to_binary_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root


root_list = [2, 3, 1, 3, 1, None, 1]
root = list_to_binary_tree(root_list)
print(Solution().pseudoPalindromicPaths(root))
