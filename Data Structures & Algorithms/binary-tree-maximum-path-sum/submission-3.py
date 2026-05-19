# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path_sum = None

    def max_path_helper(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left_sum = self.max_path_helper(root.left)
        right_sum = self.max_path_helper(root.right)
        
        max_single_path = max(root.val, root.val + max(left_sum, right_sum))
        max_top_path = max(max_single_path, root.val + left_sum + right_sum)
        self.max_path_sum = max(self.max_path_sum if self.max_path_sum is not None else max_top_path, max_top_path)
        return max_single_path

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum = None
        self.max_path_helper(root)
        return self.max_path_sum
    