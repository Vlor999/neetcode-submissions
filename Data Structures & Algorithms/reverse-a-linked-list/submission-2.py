# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prec = None
        curr = head
        if not head:
            return
        next = head.next
        while next:
            curr.next = prec
            prec = curr
            curr = next
            print(curr.val)
            next = next.next
        curr.next = prec
        return curr
        