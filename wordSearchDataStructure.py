class Tree:
    def __init__(self, char = None, children = None, isFinal = False): 
        self.char = char
        self.children = [] if children is None else children
        self.isFinal = isFinal # denotes the end of a word in the trie

    def __str__(self): # terrible, does not properly represent the tree
        string = ""
        depth = 0
        queue = [(self, 0)] # node, startIdx
        while queue:
            newQ = []
            line = ""
            nextIdx = 0
            for q in queue:
                node, startIdx = q
                line += node.char + (' ' * depth)
                for c in node.children:
                    newQ.append((c, startIdx + 1))
            queue = newQ
            depth += 1
            string += '\n'
        return string

class WordDictionary:
    def __init__(self):
        self.trie = Tree(char = '#')

    def __str__(self):
        return str(self.trie)
    
    def addWord(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            letterExists = False
            for node in curr.children:
                if node.char == letter:
                    newNode = node
                    letterExists = True
                    break
            if not letterExists:
                newNode = Tree(char = letter)
                curr.children.append(newNode)
            curr = newNode
        curr.isFinal = True # the last node to be added/"discovered" corresponds to the final letter in the word we are adding
        # as such, isFinal = True for that node
        
    def search(self, word: str) -> bool: # DFS will be more efficient than BFS (in the average cas and not necessarily asymptotically)
        # iterative DFS, more efficient than recursion
        stack = [(-1, self.trie)] # generally a valid wordIdx Tree Node pointer pair. Initialize to store root and an unreasonable word Idx
        while stack:
            wordIdx, node = stack.pop()
            charToMatch = word[wordIdx + 1] # assumes wordIdx is always less than len(word) - 1
            for c in node.children:
                if c.char == charToMatch or charToMatch == '.':
                    if (wordIdx + 1 == len(word) - 1) and c.isFinal:
                        return True
                    elif wordIdx + 1 < len(word) - 1:
                        stack.append((wordIdx + 1, c))
        return False
