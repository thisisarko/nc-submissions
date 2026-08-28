# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, count):
    if not node:
        return 0
    
    return max(count, dfs(node.left) + dfs(node.right))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            h_left = dfs(node.left)
            h_right = dfs(node.right)
            self.res = max(self.res, h_left + h_right)
            return max(h_left, h_right) + 1
        
        dfs(root)
        return self.res
        
        
        