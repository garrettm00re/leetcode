class Node:
    def __init__(self, last = None, nextN = None, value = None, idx = None):
        self.last, self.next = last, nextN
        self.val = value
        self.idx = idx
    
    def __str__(self):
        return f"Node(val = {self.val}, idx = {self.idx})"

class Mini:
    def __init__(self, nums):

        self.dict = {}
        sIdx = sorted([i for i in range(len(nums))], key = lambda x: nums[x])
        self.head = Node(value = "HEAD")
        curr = self.head
        for idx in sIdx:
            new = Node(last = curr, nextN = None, value = nums[idx], idx = idx)
            self.dict[idx] = new
            curr.next = new
            curr = new
        self.last = Node(last = curr, nextN = None, value = "LAST")
        curr.next = self.last

    
    def remove(self, idx):
        #print("removing idx", idx)
        if idx in self.dict:
            node = self.dict[idx] # all nodes in dict have a last, not necessarily a next node
            #print(node, 'REMOVING')
            #print(node.last, node.next)
            node.last.next = node.next
            node.next.last = node.last
            del self.dict[idx]
    
    def add(self, idx, val):
        curr = self.last
        nextN = (self.last).last
        while nextN.val != "HEAD" and not nextN.val < val: # <=, < -- negligable difference
            nextN = nextN.last

        new = Node(nextN, self.last, value = val, idx = idx)

        #print(f"ADDING {new} after {nextN}")
        # I believe there will be issues without this
        toDelete = nextN.next
        while toDelete.val != "LAST":
            delIdx = toDelete.idx
            del self.dict[delIdx]
            toDelete = toDelete.next


        nextN.next = new
        self.dict[idx] = new
        self.last.last = new ### was missing


    def getMin(self):
        return self.head.next.val
    
    def __str__(self):
        ret = ""
        curr = self.head
        while curr.next.val != "LAST":
            ret += f"{curr.next}, "
            curr = curr.next
        return ret




if __name__ == "__main__":
    pass