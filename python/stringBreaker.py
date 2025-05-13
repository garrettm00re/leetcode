# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

def checkIfCanBreak(s1: str, s2: str) -> bool:
    s1, s2 = ''.join(sorted(s1)), ''.join(sorted(s2))
    compare = None
    for c1, c2 in zip(s1, s2):
        if not compare and c1 != c2:
            compare = -1 if c1 < c2 else 1
        elif c1 > c2 and compare != 1:
            return False
        elif c1 < c2 and compare != -1:
            return False
    return True