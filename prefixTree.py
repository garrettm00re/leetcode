#https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=leetcode-75
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("word")
# param_2 = obj.search("word")
# param_3 = obj.startsWith("prefix")
