class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue = [root]
    rsv = []
    while queue:
        newQueue = []
        for idx, q in enumerate(queue):
            if idx == len(queue) - 1:
                rsv.append(q.val)
            if q.left:
                newQueue.append(q.left)
            if q.right:
                newQueue.append(q.right)
        queue = newQueue
    return rsv