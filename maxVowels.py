#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
def maxVowels(s: str, k: int) -> int:
    n = len(s)
    if n < k:
        return 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    start = 1
    numVowels = 0
    numVowels = sum([1 for char in s[:k] if char in vowels])
    MNV = numVowels
    new = start + k - 1
    while new < n:
        if s[start - 1] in vowels:
            numVowels -= 1
        if s[new] in vowels:
            numVowels += 1
        if numVowels > MNV: # changing this from MNV = max(MNV, numVowels) leads to a significant speed boost ==> variable assignment is more time consuming than if suite eval
            MNV = numVowels
        start += 1
        new = start + k - 1
    return MNV
