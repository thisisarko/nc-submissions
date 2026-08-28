# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            for i in range(qlen):
                n = q.popleft()
                if i == 0:
                    res.append(n.val)
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
        return res