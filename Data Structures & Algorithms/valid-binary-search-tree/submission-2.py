# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidRec(root):
            if root == None :
                return [True, float("-inf"), float("inf")]
            
            leftRoot = root.left
            leftInfo = isValidRec(leftRoot)
            rightRoot = root.right
            rightInfo = isValidRec(rightRoot)

            maxLeft = leftInfo[1] 
            minRight = rightInfo[2]
            isGood = leftInfo[0] and rightInfo[0] and maxLeft < root.val < minRight

            newMaxLeft = max(root.val, rightInfo[1])
            newMinRight = min(root.val, leftInfo[2])

            return [isGood, newMaxLeft, newMinRight]
        val = isValidRec(root)
        return val[0]
