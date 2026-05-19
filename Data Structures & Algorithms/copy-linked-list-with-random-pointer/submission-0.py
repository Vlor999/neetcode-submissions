"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        first = head
        newHead = Node(head.val)
        cop = newHead
        copFin = newHead
        listElem = {head: newHead}
        
        while first.next:
            first = first.next
            newHead.next = Node(first.val)
            newHead = newHead.next
            listElem[first] = newHead
        
        second = head
        cop = copFin
        while cop and second:
            rand = second.random
            cop.random = listElem.get(rand, None)
            cop = cop.next
            second = second.next
        
        return copFin
        