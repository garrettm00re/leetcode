
#https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowCounter = {} # key = row tuple, val = # instances
        pairs = 0
        n = len(grid)
        for row in grid:
            key = tuple(row)
            if not key in rowCounter:
                rowCounter[key] = 0
            rowCounter[key] += 1
        
        for colIdx in range(n): # n x n
            key = tuple(grid[i][colIdx] for i in range(n))
            if key in rowCounter:
                pairs += rowCounter[key]

        return pairs