class Solution:
    def mergeList(self, l1, l2):
        if not l1 and not l2 :
            return None 
        output = ListNode()
        head = output
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            if val1 < val2:
                output.val = val1
                l1 = l1.next
            else :
                output.val = val2
                l2 = l2.next
            output.next = ListNode()
            output = output.next
        if l1 != None:
            output.val = l1.val
            output.next = l1.next
        if l2 != None:
            output.val = l2.val
            output.next = l2.next
        return head

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        taille = len(lists)
        if taille > 2:
            mid = taille // 2
            l1, l2 = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
            return self.mergeList(l1, l2)
        elif taille == 2:
            return self.mergeList(lists[0], lists[1])
        else :
            return lists[0] if taille == 1 else None