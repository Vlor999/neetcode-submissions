# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        out = ListNode()
        head_out = out
        while head1 and head2:
            if head1.val < head2.val:
                out.next = head1
                head1 = head1.next
            else:
                out.next = head2
                head2 = head2.next
            out = out.next
        if head1:
            out.next = head1
        if head2:
            out.next = head2
        return head_out.next

