"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        m = {}
        ptr = head
        while ptr is not None:
            m[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        for k, v in m.items():
            nxt = k.next
            rnd = k.random
            v.next = m.get(nxt)
            v.random = m.get(rnd)
        
        return m[head]