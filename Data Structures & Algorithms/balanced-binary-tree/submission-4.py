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
        # left section
        leftHeight = self.getHeight(root.left)
        prevLeft = self.isBalanced(root.left)

        # right section
        rightHeight = self.getHeight(root.right)
        prevRight = self.isBalanced(root.right)

        isPrevValide = prevRight and prevLeft
        return isPrevValide and abs(rightHeight - leftHeight) <= 1