# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def copy_and_invert(r):
            if r is None:
                return
            node = TreeNode(r.val)
            node.left, node.right = copy_and_invert(r.right), copy_and_invert(r.left)
            return node
        new_root = copy_and_invert(root)
        return new_root
        
        

        