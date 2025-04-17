#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root  # Base case: found p or q or reached the end
        
        left = self.lowestCommonAncestor(root.left, p, q)  # Search left subtree
        right = self.lowestCommonAncestor(root.right, p, q)  # Search right subtree
        
        if left and right:  
            return root  # If p and q are found in different subtrees, root is LCA
        
        return left if left else right  # Return the non-null subtree (or None if neither found)