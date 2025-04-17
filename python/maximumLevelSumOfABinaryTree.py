# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        maxSum, maxLevel = -float("inf"), 0
        currLayer = 1
        while queue:
            newQueue = []
            layerSum = 0
            for node in queue:
                layerSum += node.val
                if node.left != None:
                    newQueue.append(node.left)
                if node.right != None:
                    newQueue.append(node.right)
            if layerSum > maxSum:
                maxSum = layerSum
                maxLevel = currLayer
            currLayer += 1
            queue = newQueue

        return maxLevel
