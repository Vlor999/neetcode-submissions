# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        setElem = set()
        while head != None:
            if head not in setElem:
                setElem.add(head)
            else:
                return True
            head = head.next
        return False
        