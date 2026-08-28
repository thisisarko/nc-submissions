# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node):
            if not node:
                return 0
            h_left = dfs(node.left)
            h_right = dfs(node.right)
            if abs(h_left - h_right) > 1:
                self.res = False
            return max(h_left, h_right) + 1
        dfs(root)
        return self.res
        