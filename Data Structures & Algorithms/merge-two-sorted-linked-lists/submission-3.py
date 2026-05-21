# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        if head1 is None and head2 is None:
            return 
        out = ListNode()
        head_out = out
        while head1 and head2:
            if head1.val < head2.val:
                value = head1.val
                head1 = head1.next
            else:
                value = head2.val
                head2 = head2.next
            out.val = value
            out.next = ListNode()
            out = out.next
        if head1:
            out.val = head1.val
            out.next = head1.next
        if head2:
            out.val = head2.val
            out.next = head2.next
        return head_out

