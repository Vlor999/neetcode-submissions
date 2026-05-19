# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        prev = ListNode(head.val, None)
        head = head.next
        while head != None:
            suiv = head.next
            prev = ListNode(head.val, prev)
            head = suiv
        return prev