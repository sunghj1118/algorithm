# 1379. Problem Review

## 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

### Problem Definition
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

### Approach
- Traverse both trees simultaneously.
- If target node is found in original tree, return corresponding node in the cloned tree.

### Solution
- Solved with DFS.
- dfs(treenode_of_original_tree, treenode_of_cloned_tree)
    - if original tree node exists:
        - if original tree node == target node:
            - self.ans = cloned_treenode
        
        - dfs(node_of_og_tree.leftnode, node_of_cloned_tree.leftnode)
        - dfs(node_of_og_tree.rightnode, node_of_cloned_tree.rightnode)
- dfs(original, closed)
- return self.ans

```python
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