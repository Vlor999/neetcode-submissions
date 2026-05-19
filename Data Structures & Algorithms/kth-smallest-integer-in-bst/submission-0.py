# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def creationList(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        leftList = self.creationList(root.left)
        midVal = root.val
        rightList = self.creationList(root.right)
        return leftList + [midVal] + rightList
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        outputList = self.creationList(root)
        return outputList[k - 1]
 