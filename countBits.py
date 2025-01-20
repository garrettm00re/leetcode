# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
# Beats 98% of users with python3

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]
    numOnes, windowSize, windowDigits, i = 0, 1, 1, 1
    while i <= n:
        numOnes = 1 + ans[i - windowSize]
        ans.append(numOnes)

        if numOnes == windowDigits:
            windowDigits += 1
            windowSize *= 2 # 2 ** (windowDigits - 1)
        i += 1
    return ans