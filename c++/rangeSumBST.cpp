#include <vector>
#include <iostream>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int totalInRange = 0;
        vector<TreeNode*> stack;
        stack.push_back(root);
        TreeNode* curr;
        while (stack.size() > 0) {
            curr = stack.back();
            stack.pop_back();
            if (curr->val <= high && curr->val >= low) {
                totalInRange += curr->val;
            }
            if (curr->left != nullptr) {
                stack.push_back(curr->left);
            }
            if (curr->right != nullptr) {
                stack.push_back(curr->right);
            }
        }
        return totalInRange;
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->right = new TreeNode(15);
    cout << solution.rangeSumBST(root, 7, 15) << endl;

    delete root->left;
    delete root->right;
    delete root;
}