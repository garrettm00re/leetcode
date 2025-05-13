# beats 98%! https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        '''
                7
                1.    4
            6     5. 3
                        2
                    for
        '''
        def dfs(node):
            if not node:
                return []
            if node.left == node.right == None:
                return [1]
            left, right = dfs(node.left), dfs(node.right)
            leaves = []
            for leaf in left + right:
                if leaf + 1 < distance:
                    leaves.append(leaf + 1)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.count += 1
                    else:
                        break
            return sorted(leaves)
        self.count = 0
        dfs(root)
        return self.count