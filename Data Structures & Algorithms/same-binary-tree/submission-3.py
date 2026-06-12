# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def linearize(self, p:TreeNode) -> list:
        if p is None:
            return []
        lin = []
        nexts = [p]
        while nexts:
            node = nexts.pop(0)
            if node:
                nexts.append(node.left)
                nexts.append(node.right)
            lin.append(node.val if node else None)
        return lin

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        linearPTree = self.linearize(p)
        linearQTree = self.linearize(q)
        return linearQTree == linearPTree
        