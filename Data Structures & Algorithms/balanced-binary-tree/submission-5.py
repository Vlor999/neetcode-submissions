class Solution:
    def getHeight(self, root: TreeNode) -> bool:
        if root is None:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return 1 + max(rightHeight, leftHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        # previsou values:
        prevLeft = self.isBalanced(root.left)
        prevRight = self.isBalanced(root.right)
        isPrevValide = prevRight and prevLeft
        if not isPrevValide:
            return False

        # left section
        leftHeight = self.getHeight(root.left)
        # right section
        rightHeight = self.getHeight(root.right)
        return abs(rightHeight - leftHeight) <= 1