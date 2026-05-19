class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_balance(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return max(left_height, right_height) + 1, balanced
        
        _, is_balanced = check_balance(root)
        return is_balanced