# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            isValid = True
            if lower is not None and node.val <= lower:
                isValid = False
            if upper is not None and node.val >= upper:
                isValid = False
            return (
                isValid
                and dfs(node.left, lower, node.val) 
                and dfs(node.right, node.val, upper)
            )
        return dfs(root, None, None)
        