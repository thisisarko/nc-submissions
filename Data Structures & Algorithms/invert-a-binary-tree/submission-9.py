# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def copySwap(node):
    if not node:
        return None
    root = TreeNode(node.val)
    root.left, root.right = copySwap(node.right), copySwap(node.left)
    return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return copySwap(root)