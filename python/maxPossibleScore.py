class Solution:
    """
    My original solution. Inelegant but faster than below. 
    """
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def possible(theoreticalMax):
            curr = low
            for i in range(1, n):
                thisRange = sortStart[i]
                newMax = curr + theoreticalMax
                if thisRange <= newMax <= thisRange + d:
                    curr = newMax
                elif newMax < thisRange:
                    curr = thisRange
                else:
                    return False
            return True

        def jumpFXN(curr, i, plus):
            jump = max(maxScore // 2 ** (i + 1), 1)
            if plus:
                return curr + jump
            else:
                return curr - jump

        n = len(start)
        sortStart = sorted(start)
        low, high = sortStart[0], sortStart[-1] + d
        maxScore = (high - low) // (n - 1)
        curr, i, maxMin = 0, 0, 0
        plus = True
        visited = set()
        while i < maxScore:
            curr = jumpFXN(curr, i, plus)
            if curr in visited:
                return maxMin
            if possible(curr):
                maxMin = max(maxMin, curr)
                plus = True
            else:
                plus = False
            visited.add(curr)
            i += 1
        return maxMin


from typing import List

class Solution:
    """
    Cleaner, traditional binary search approach. Somehow slower. 
    """
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def is_possible(min_diff: int) -> bool:
            last = float('-inf')
            for s in start:
                if last + min_diff > s + d:
                    return False
                last = max(s, last + min_diff)
            return True

        start.sort()
        left, right = 0, (start[-1] + d) - start[0]
        while left < right:
            mid = (left + right + 1) // 2
            if is_possible(mid):
                left = mid
            else:
                right = mid - 1
        return left
