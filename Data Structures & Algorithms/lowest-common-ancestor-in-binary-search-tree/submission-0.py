# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ptr1 = root
        ptr2 = root
        # p and q both exist in the tree, so the values will always be found

        s1 = [ptr1]
        s2 = [ptr2]
        while ptr1.val != p.val:
            if p.val < ptr1.val:
                ptr1 = ptr1.left
            else:
                ptr1 = ptr1.right
            s1.append(ptr1)

        while ptr2.val != q.val:
            if q.val < ptr2.val:
                ptr2 = ptr2.left
            else:
                ptr2 = ptr2.right
            s2.append(ptr2)
        
        first_idx = min(len(s1), len(s2)) - 1
        for i in range(first_idx, -1, -1):
            if s1[i] == s2[i]:
                return s1[i]
        return None

        