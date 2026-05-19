# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        mainList = []
        def levelOrderNiveau(root: TreeNode, currentLevel=0):
            if root is None:
                return
            if len(mainList) == currentLevel:
                mainList.append(root.val)
            levelOrderNiveau(root.right, currentLevel + 1)
            levelOrderNiveau(root.left, currentLevel + 1)
        levelOrderNiveau(root, 0)
        return mainList