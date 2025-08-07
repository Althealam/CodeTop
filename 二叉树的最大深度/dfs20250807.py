# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node, current_path_depth):
        if not node:
            return current_path_depth
        return max(self.dfs(node.left, current_path_depth+1), self.dfs(node.right, current_path_depth+1))

        