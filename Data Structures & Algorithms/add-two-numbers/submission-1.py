# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def sum_vals(val1, val2, carry=0):
    sm = (val1 + val2 + carry) % 10
    new_carry = 1 if (val1 + val2 + carry) >= 10 else 0
    return (val1 + val2 + carry) % 10, new_carry


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        p1 = l1
        p2 = l2

        newHead = ListNode()
        p3 = newHead
        carry = 0

        while p1 or p2 or carry:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0

            s, c = sum_vals(p1_val, p2_val, carry)
            p3.val = s
            carry = c

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            
            if p1 or p2 or carry:
                p3.next = ListNode()
                p3 = p3.next
        
        return newHead
        
