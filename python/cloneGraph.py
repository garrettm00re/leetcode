from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clonedNodes = {}

        def dfs(node):
            if node.val in clonedNodes:
                return clonedNodes[node.val]

            clonedNodes[node.val] = Node(node.val)  # Clone the node
            for neighbor in node.neighbors:
                clonedNodes[node.val].neighbors.append(dfs(neighbor))  # Directly append the cloned neighbors

            return clonedNodes[node.val]

        dfs(node)
        return clonedNodes[node.val]