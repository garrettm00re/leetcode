# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

def numSplits(self, s):
    """
    :type s: str
    :rtype: int
    """
    def add(dictionary, el):
        if not char in dictionary:
            dictionary[char] = 0
        dictionary[char] += 1
        return dictionary

    def remove(dictionary, char):
        dictionary[char] -= 1
        if dictionary[char] == 0:
            del dictionary[char]
        return dictionary

    numGood = 0
    if len(s) > 1:
        left, right = {}, {}
        for char in s:
            right = add(right, char)

        for char in s:
            left = add(left, char)
            right = remove(right, char)
            numGood += 1 if len(left.keys()) == len(right.keys()) else 0
    return numGood
        