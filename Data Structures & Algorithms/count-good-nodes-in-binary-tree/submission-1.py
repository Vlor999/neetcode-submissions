# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isGood(self, root: TreeNode, listPrec:list[TreeNode]) -> bool:
        currentVal = root.val
        for elem in listPrec:
            if elem.val > currentVal:
                return False
        return True

    def goodNotesRec(self, root: TreeNode, listPrec: list[TreeNode]) -> int:
        if root == None:
            return 0
        currentGood = self.isGood(root, listPrec)
        newList = listPrec + [root]
        compteGauche = self.goodNotesRec(root.left, newList)
        compteDroit = self.goodNotesRec(root.right, newList)
        return currentGood + compteGauche + compteDroit
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNotesRec(root, [])
        