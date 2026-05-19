# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currentVal = root.val
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        if minVal <= currentVal <= maxVal:
            return root
        if maxVal > root.right.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)
        