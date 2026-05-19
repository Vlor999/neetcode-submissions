# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def depth(self, node: TreeNode) -> int:
        if not node:
            return 0
        leftDepth = self.depth(node.left)
        rightDepth = self.depth(node.right)
        self.diameter = max(self.diameter, leftDepth + rightDepth)
        return max(leftDepth, rightDepth) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.diameter