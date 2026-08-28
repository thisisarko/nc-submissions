# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0
            bleft, hleft = dfs(node.left)
            bright, hright = dfs(node.right)
            balanced = bleft and bright and abs(hleft - hright) < 2
            return balanced, max(hleft, hright) + 1
        return dfs(root)[0]
        