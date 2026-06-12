# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        leftPart = self.invertTree(root.left)
        rightPart = self.invertTree(root.right)
        root.right = leftPart
        root.left = rightPart
        return root
 