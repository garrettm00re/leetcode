# https://leetcode.com/problems/edit-distance/
# see also: https://leetcode.com/problems/edit-distance/solutions/6210672/beats-92-simple-intuitive-solution-in-py-3jww

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    def EDIT(i, j):
        # i and j are the first indicies of the substrings to edit
        if (i, j) in cache:
            return cache[(i, j)]
        if i > len(word1) - 1 or j > len(word2) - 1:
            if i > len(word1) - 1 and j > len(word2) - 1:
                return 0
            incomplete = len(word1) - i if i < len(word1) else len(word2) - j
            return incomplete # don't bother caching because if else executes in O(1)
        if word1[i] == word2[j]:
            cache[(i, j)] = EDIT(i + 1, j + 1)
        else:
            cache[(i, j)] = 1 + min(EDIT(i, j + 1), EDIT(i + 1, j), EDIT(i + 1, j + 1))
        
        return cache[(i, j)]
    
    cache = {} # key = (i, j), value = EDIT(word1[i:], word2[j:])
    return EDIT(0, 0)