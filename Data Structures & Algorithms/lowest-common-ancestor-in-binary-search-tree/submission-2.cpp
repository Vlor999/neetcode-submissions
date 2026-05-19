/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int minVal = min(p->val, q->val);
    int maxVal = max(p->val, q->val);
    int currentVal = root->val;
    if (minVal <= currentVal && currentVal <= maxVal){
        return root; 
    }
    if (root->right != nullptr && maxVal > root->right->val){
        return lowestCommonAncestor(root->right, p, q);
    }
    return lowestCommonAncestor(root->left, p, q);
    }
};
