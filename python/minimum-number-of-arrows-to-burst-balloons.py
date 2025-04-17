# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# NOTE TO SELF:
# see solutions (in order of submission) on LC to see the evolution of my thought process. 
# the final improvement is the most brilliant, but you did most of the work (time complexity wise) before then


import heapq
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort points by their end coordinates instead of start coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 0
        minEnd = float('-inf')  # Initialize to negative infinity
        
        for start, end in points:
            if start > minEnd:
                # If the current balloon starts after the last arrow's range, shoot a new arrow
                arrows += 1
                minEnd = end  # Update the range of the new arrow
                
        return arrows