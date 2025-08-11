# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 链：从子树中的叶子节点到当前节点的路径。空节点的链长尾-1，叶子节点的链长为0
# 直径：等价于两条链拼接成的路径
# 枚举每个node，假设直径在这里拐弯，也就是计算由左右两条从下面的叶子节点到node的链的节点值

# 思路：在当前节点拐弯的直径长度=左子树的最长链+右子树的最长链
# 返回给父节点的是以当前节点为根的子树的最长链=max(左子树的最长链，右子树的最长链)+1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 # 最长直径
        def dfs(node):
            if node is None: # 空节点的链长为-1
                return -1
            if node.left is None and node.right is None: # 叶子节点的链长为0
                return 0
            nonlocal ans # 表示ans在函数内有效
            l_len = dfs(node.left)+1 # 左子树的最长链
            r_len = dfs(node.right)+1 # 右子树的最长链
            ans = max(ans, l_len+r_len)  # 更新二叉树的最长直径
            return max(l_len, r_len)
        dfs(root)
        return ans
        