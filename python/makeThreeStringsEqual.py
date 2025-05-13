# https://leetcode.com/problems/make-three-strings-equal/

def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
    mLen = min(len(s1), len(s2), len(s3))
    i = -1
    while i + 1 < mLen and s1[i + 1] == s2[i + 1] == s3[i + 1]:
        i += 1
    if i == -1:
        return -1
    else:
        # o1 = len(s1) - (i + 1)
        # o2 = len(s2) - (i + 1)
        # o3 = len(s3) - (i + 1)
        return len(s1) + len(s2) + len(s3) - 3 * (i + 1)