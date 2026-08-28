# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(r1, r2):
    if not (r1 or r2):
        return True
    if r1 and r2 and r1.val == r2.val:
        return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
    else:
        return False

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        else:
            return (
                self.isSubtree(root.left, subRoot)
                or 
                self.isSubtree(root.right, subRoot)
            )
        