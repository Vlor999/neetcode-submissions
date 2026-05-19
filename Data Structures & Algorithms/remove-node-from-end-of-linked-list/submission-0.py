# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        compte = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            compte += 2
        
        if fast:
            compte += 1
        
        pos = 0
        target = compte - n
        prev, current = None, head
        while pos != target:
            prev = current
            current = current.next
            pos += 1
        
        if prev:
            prev.next = current.next if current else None 
        else :
            head = head.next if head else None

        return head
        