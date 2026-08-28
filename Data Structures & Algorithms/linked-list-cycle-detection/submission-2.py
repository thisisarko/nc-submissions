# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while slow and fast:
            if not slow.next:
                return False
            if not (fast.next and fast.next.next):
                return False
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
        return False
