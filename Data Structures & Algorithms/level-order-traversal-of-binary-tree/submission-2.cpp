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
    void levelOrderLevel(TreeNode* root, int level, vector<vector<int>>& mainVector) {
        if (root == nullptr) {
            return;
        }
        int taille = mainVector.size();
        if (taille > level) {
            mainVector[level].push_back(root->val);
        } else {
            mainVector.push_back(vector<int> {root->val});
        }
        levelOrderLevel(root->left, level + 1, mainVector);
        levelOrderLevel(root->right, level + 1, mainVector);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> mainVector;
        levelOrderLevel(root, 0, mainVector);
        return mainVector;
    }
};