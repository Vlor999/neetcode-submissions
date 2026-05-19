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
    tuple<int,bool> stepBalanceHeight(TreeNode* root){
        if (root == nullptr){
            tuple<int,bool> val = {0, true};
            return val;
        }
        tuple<int,bool> leftInfo = stepBalanceHeight(root->left);
        tuple<int,bool> rightInfo = stepBalanceHeight(root->right);
        tuple<int,bool> outputInfo = {max(get<0>(leftInfo), get<0>(rightInfo)) + 1, get<1>(leftInfo) && get<1>(rightInfo) && abs(get<0>(leftInfo) - get<0>(rightInfo)) <= 1};
        return outputInfo;
    }
    bool isBalanced(TreeNode* root) {
        tuple<int,bool> output = stepBalanceHeight(root);
        return get<1>(output);
    };
};

