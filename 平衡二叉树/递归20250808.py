# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        h = abs(self.get_height(root.left)-self.get_height(root.right))<=1
        if h == True:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def get_height(self, node):
        if node is None:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right))+1