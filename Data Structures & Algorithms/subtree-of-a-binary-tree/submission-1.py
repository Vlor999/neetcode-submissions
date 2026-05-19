# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False
        if p == None and q == None:
            return True
        if p.val != q.val:
            return False
        isGoodLeft = self.isSameTree(p.left, q.left)
        isGoodRight = self.isSameTree(p.right, q.right)
        return isGoodLeft and isGoodRight

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot == None:
            return True
        if root == None:
            if subRoot == None:
                return True
            return False
        isGoodHere = self.isSameTree(root, subRoot)
        isGoodLeft = self.isSameTree(root.left, subRoot)
        isGoodRight = self.isSameTree(root.right, subRoot)
        isGood = isGoodHere or isGoodLeft or isGoodRight
        if isGood:
            return isGood
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)