# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([(1, root)])
        while q:
            l, n = q.popleft()
            last_level = len(res)
            if last_level == l:
                res[-1].append(n.val)
            else:
                # handles the one edge case where last_level < l
                res.append([n.val])
            if n.left:
                q.append((l+1, n.left))
            if n.right:
                q.append((l+1, n.right))
        return res