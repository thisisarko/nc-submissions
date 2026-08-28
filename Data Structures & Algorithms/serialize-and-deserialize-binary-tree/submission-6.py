# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return json.dumps([])
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('N')
        if res and res[-1] == 'N':
            while res[-1] == 'N':
                res.pop()
        return json.dumps(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = json.loads(data)

        if not vals:
            return None

        root = TreeNode(vals[0])
        q = deque([root])

        i = 1

        while q and i < len(vals):
            node = q.popleft()

            if vals[i] != 'N':
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != 'N':
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1

        return root

