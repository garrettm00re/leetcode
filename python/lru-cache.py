#https://neetcode.io/problems/lru-cache
class LRUCache:
    # attempt two !
    def __init__(self, capacity):
        self.head = Node()
        self.keyNode = {} # key: Node
        self.last = self.head
        self.capacity = capacity
        self.size = 0

    def remove(self, key): # head will never be removed, so safe to assume it's always there
        toRemove = self.keyNode[key]
        prev = toRemove.prev
        nex = toRemove.nex
        # remove the node from the linked list structure
        if nex != None:
            nex.prev = prev
        prev.nex = nex # this is ok even if nex is None
        del self.keyNode[key] # remove the node from the dict
        if toRemove == self.last:# update last so no iteration is necessary to add to the end
            self.last = prev
        self.size -= 1 

    def addEnd(self, key, value):
        print(key, value)
        print([(key, self.keyNode[key].value) for key in self.keyNode.keys()])
        newLast = Node(key, value)
        oldLast = self.last
        oldLast.nex = newLast
        newLast.prev = oldLast
        self.last = newLast
        self.keyNode[key] = newLast
        self.size += 1

    def get(self, key):
        if key in self.keyNode:
            node = self.keyNode[key]
            self.remove(key)
            self.addEnd(key, node.value)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.keyNode:
            self.remove(key)
            self.addEnd(key, value)
        else:
            if self.size == self.capacity:
                LRU = self.head.nex
                self.remove(LRU.key)
            self.addEnd(key, value)
class Node:
    def __init__(self, key = None, value = None):
        self.key = key # I don't need the key at all, but whatever
        self.value = value
        self.prev = None
        self.nex = None

class LRUCacheAttemptOne: # keeping this to detail my thought process

    def __init__(self, capacity: int):
        self.numOps = 0
        self.capacity = capacity
        self.timeKey = {}  ##### no # minheap
        self.keyTime = {}
        self.keyValue = {}
        # lru = numOps - capacity

    def updateTime(self, key: int):
        #update recency
        self.numOps += 1
        currTime = self.numOps
        # get and update last time
        lastTime = self.keyTime[key]
        self.keyTime[key] = currTime
        #update time key (this makes put run in O(1))
        del self.timeKey[lastTime]
        self.timeKey[currTime] = key
    
    def add(self, key: int, value: int):
        # add key to LRU cache
        print(f"adding key: {key} value: {value}")
        self.numOps += 1
        self.keyValue[key] = value
        self.keyTime[key] = self.numOps
        self.timeKey[self.numOps] = key

    def get(self, key: int) -> int:
        self.checkState()
        print(f"getting key: {key}")
        print()
        if key in self.keyValue:
            mru = self.timeKey[self.numOps]
            if not key == mru:
                self.updateTime(key) ## update time
            return self.keyValue[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.checkState()
        if key in self.keyValue:
            print("update")
            self.keyValue[key] = value
            self.updateTime(key)
        else:
            if len(self.keyValue) < self.capacity:
                self.add(key, value)
            else:
                lru = self.numOps - self.capacity + 1 # the plus one is because I add the first element with time 1
                removeKey = self.timeKey[lru]
                print(f"removing {removeKey}, which was placed/updated at time {lru}")
                # remove lru
                del self.timeKey[lru]
                del self.keyValue[removeKey]
                del self.keyTime[removeKey]

                # add new key value pair
                self.add(key, value)
        print()
    def checkState(self):
        print("TIME KEY", self.timeKey)
        print("KEY VALUE", self.keyValue)
        print("KEY TIME", self.keyTime)


        
