#https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mPath = -float("inf")): # could be further optimized with a max stack (not doing that today)
            if node == None:
                return 0
            value = 1 if node.val >= mPath else 0
            for child in (node.left, node.right):
                value += dfs(child, max(mPath, node.val))
            return value
        return dfs(root)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        good_nodes = 0
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                good_nodes += 1
                max_val = node.val
            if node.right:
                stack.append((node.right, max_val))
            if node.left:
                stack.append((node.left, max_val))
        return good_nodes