# leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Elegant solution (not my own, but I've added comments that explain the improvements it makes over mine)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return float("inf")
            return (y1-y2)/(x1-x2)
        
        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int) # resetting the slopes for each point simplifies logic substantially.
            # means we don't have to compute y intercept as all p2 are relative to p1 (and thus slope specifies the line)
            for j, p2 in enumerate(points[i+1:]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1
    
# UGLY SOLUTION --> functional, based on the right ideas, but inelegant and overly complicated
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lookup = {} # key = (slope, intercept) value = [minX, corrY] , [maxX, corrY] (tie = minY)
        n = len(points)
        if n <= 2:
            return n
        longestLine = 1

        for idx in range(len(points) - 1):
            for jdx in range(idx + 1, len(points)):
                p1, p2 = points[idx], points[jdx]
                if p2[0] - p1[0]:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    intercept = p2[1] - (slope * p2[0])
                else:
                    slope = float("inf")
                    intercept = p1[0]
                    # could be division errors, so round if they arise
                tuP1, tuP2 = tuple(p1), tuple(p2)
                key = (slope, intercept)
                if not key in lookup:
                    lookup[key] = set()
                lookup[key].add(tuple(p1))
                lookup[key].add(tuple(p2))
                longestLine = max(len(lookup[key]), longestLine)
        return longestLine
    