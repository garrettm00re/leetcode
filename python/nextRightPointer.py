
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next # next right node (same depth level)

def connectElegant(root):
    """
    This version uses O(1) space and O(V) time. It is the cleanest version of the three below.
    """
    if not root:
        return None

    parent = root

    while parent:
        dummy = Node(0)
        tail = dummy
        curr = parent

        while curr:
            if curr.left:
                tail.next = curr.left
                tail = tail.next
            if curr.right:
                tail.next = curr.right
                tail = tail.next
            curr = curr.next

        parent = dummy.next
    return root
def connect(root):
    """
    This version uses O(1) space and O(V) time.
    """
    parent = root
    last = None
    curr = None
    leftmost = None

    while parent:
        currStack = []
        if parent.left and parent.right:
            currStack = [parent.left, parent.right]
        elif parent.right:
            currStack = [parent.right]
        elif parent.left:
            currStack = [parent.left]
        for curr in currStack:
            if last == None:
                leftmost = curr
            else:
                last.next = curr
            last, curr = curr, None

        parent = parent.next

        if parent == None and leftmost != None:
            # this implies we have finished the current level
            parent = leftmost # reinitialize the level order traversal with the leftmost tree node
            last = None
            curr = None
            leftmost = None
    return root

def connectNoSpaceLimit(root):
    """
    :type root: Node
    :rtype: Node
    """
    queue = [root] if root else []
    while queue:
        newQueue = []
        for i in range(len(queue)):
            curr = queue[i]
            if i + 1 == len(queue):
                nextNode = None
            else:
                nextNode = queue[i + 1]
            curr.next = nextNode
            if curr.left:
                newQueue.append(curr.left)
            if curr.right:
                newQueue.append(curr.right)
        queue = newQueue
    return root