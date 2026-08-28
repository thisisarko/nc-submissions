# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def findMiddle(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(node):
    prev, curr = None, node
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def merge(node1, node2):
    p1 = node1
    p2 = node2
    while p1 and p2:
        temp = p1.next
        p1.next = p2
        p2 = p2.next
        p1.next.next = temp
        p1 = temp




class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        middle = findMiddle(head)
        rev = reverse(middle.next)
        middle.next = None
        merge(head, rev)




