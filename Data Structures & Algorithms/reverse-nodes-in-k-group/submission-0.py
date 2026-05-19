# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode, limit: int) -> tuple:
        if head is None:
            return None, None
        
        count = 0
        current = head
        while current and count < limit:
            current = current.next
            count += 1
            
        if count < limit:
            return head, None
        
        prev = None
        current = head
        nextNode = None
        count = 0
        
        while current and count < limit:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
            count += 1
            
        head.next = nextNode
        return prev, nextNode
    
    def getEnd(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        while head.next:
            head = head.next
        return head
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1:
            return head
            
        copyHead = ListNode(0)
        copyHead.next = head
        prevGroupEnd = copyHead
        
        while True:
            groupStart = prevGroupEnd.next
            if not groupStart:
                break
            newGroupStart, nextGroupStart = self.reverseList(groupStart, k)
            if newGroupStart == groupStart:
                break
            prevGroupEnd.next = newGroupStart
            prevGroupEnd = groupStart
            
            if not nextGroupStart:
                break
        
        return copyHead.next

