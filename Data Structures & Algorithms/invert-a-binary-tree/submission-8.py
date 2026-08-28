# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def swap(node):
    if not node:
        return
    node.left, node.right = node.right, node.left

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        swap(root)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
