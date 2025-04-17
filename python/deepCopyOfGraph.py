class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node):
    copies = {}
    def copy(node):
        print(node.val if node else None)
        if node in copies:
            return copies[node]
        if node:
            copies[node] = []
            copies[node] = Node(node.val, [copy(n) for n in node.neighbors if copy(n)])
            return copies[node]     
    return copy(node)