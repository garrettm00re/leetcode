# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    firstUnused = 0
    for sChar in s:
        found = False
        if firstUnused < len(t):
            for idx, tChar in enumerate(t[firstUnused:]):
                if tChar == sChar:
                    found = True
                    firstUnused += idx + 1
                    break
        if not found:
            return False
    return True