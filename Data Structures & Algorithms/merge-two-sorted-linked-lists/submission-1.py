# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        if not list2:
            return list1
        if not list1:
            return list2

        
        res = ListNode()

        p1 = list1
        p2 = list2
        r = res
        while p1 and p2:
            if p1.val <= p2.val:
                r.next = p1
                p1 = p1.next
            else:
                r.next = p2
                p2 = p2.next
            r = r.next
        r.next = p1 or p2
        
        res = res.next
        return res

