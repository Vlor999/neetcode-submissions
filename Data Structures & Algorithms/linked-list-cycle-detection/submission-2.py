# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head
        while first:
            first = first.next
            if first:
                first = first.next
            else:
                return False
            second = second.next
            if first == second:
                return True
        return False