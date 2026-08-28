# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Max Depth at node = max(maxDepth(node.left), maxDepth(node.right)) + 1
# Base case: both node.left and node.right are null, return 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        


        