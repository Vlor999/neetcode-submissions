# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
            
        if list1.val < list2.val:
            output = ListNode(list1.val, None)
            list1 = list1.next
        else:
            output = ListNode(list2.val, None)
            list2 = list2.next
        
        head = output

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                newVal = ListNode(list1.val, None)
                list1 = list1.next
            else:
                newVal = ListNode(list2.val, None)
                list2 = list2.next
            
            output.next = newVal
            output = output.next
        
        if list1 != None : 
            output.next = list1
        if list2 != None:
            output.next = list2
        
        return head