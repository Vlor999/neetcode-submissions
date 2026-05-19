# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = 0
        val2 = 0
        pos = 0
        while l1:
            val1 = val1 + l1.val * 10 ** pos 
            l1 = l1.next
            pos += 1
        pos = 0
        while l2:
            val2 = val2 + l2.val * 10 ** pos 
            l2 = l2.next
            pos += 1
        val = str(val1 + val2)[::-1]
        head = ListNode()
        curr = head
        for chiffre in val[:-1]:
            head.val = int(chiffre)
            head.next = ListNode()
            head = head.next
        
        head.val = val[-1]
        
        return curr


