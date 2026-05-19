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
bool isGood(TreeNode* root, int maxValuePrec){
    return root->val >= maxValuePrec;
}

int goodNotesRec(TreeNode* root, int maxValuePrec){
    if (root == nullptr){
        return 0;
    }
    bool isCurrentGoodNode = isGood(root, maxValuePrec);
    int newMax = max(root->val, maxValuePrec);
    int nombreGoodNodeRight = goodNotesRec(root->right, newMax);
    int nombreGoodNodeLeft = goodNotesRec(root->left, newMax);
    return nombreGoodNodeLeft + nombreGoodNodeRight + (isCurrentGoodNode ? 1 : 0);
}
    int goodNodes(TreeNode* root) {
        return goodNotesRec(root, INT_MIN);
    }
};