# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def copyInvert(node):
    if not node:
        return None
    root = TreeNode(node.val)
    root.left, root.right = copyInvert(node.right), copyInvert(node.left)
    return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return copyInvert(root)