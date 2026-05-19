# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isGood(self, root: TreeNode, maxPrec:int) -> bool:
        return root.val >= maxPrec

    def goodNotesRec(self, root: TreeNode, maxPrec) -> int:
        if root == None:
            return 0
        currentGood = self.isGood(root, maxPrec)
        newMax = max(maxPrec, root.val)
        compteGauche = self.goodNotesRec(root.left, newMax)
        compteDroit = self.goodNotesRec(root.right, newMax)
        return currentGood + compteGauche + compteDroit
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNotesRec(root, float('-inf'))