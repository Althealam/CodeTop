# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        path = []
        self.traversal(root, res, path, targetSum)
        if len(res)!=0:
            return True
        return False
    
    def traversal(self, root, res, path, targetSum):
        if not root:
            return None
        path.append(root.val)
        if root.left is None and root.right is None and sum(path[:])==targetSum:
            res.append(path[:])
            return 
        if root.left:
            self.traversal(root.left, res, path, targetSum)
            path.pop()
        if root.right:
            self.traversal(root.right, res, path, targetSum)
            path.pop()