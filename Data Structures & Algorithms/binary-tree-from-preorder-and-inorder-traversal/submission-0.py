# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# In a preorder, the first element is the root of the tree ebign inspected.
# Inorder reprn will contain all values of the left subtree to the left
# of the root index and the values of the right subtree to the right.

# > Both arrays are of the same size and consist of unique values.
# Unique values: This means when searching for an element in the inorder
# array, we are guaranteed to get only one occurence which uniquely
# identifies the root from the preorder.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return None
        
        val = preorder[0]
        root = TreeNode(val)
        rootPosInorder = inorder.index(val)
        root.left = self.buildTree(
            preorder[1 : rootPosInorder + 1],
            inorder[ : rootPosInorder]
        )
        root.right = self.buildTree(
            preorder[rootPosInorder + 1 :],
            inorder[rootPosInorder + 1 :]
        )
        return root
