# leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = [0] * len(temperatures)  # Optimized list initialization
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answers[prev] = idx - prev
            stack.append(idx)
        return answers


### NOTE s:
# elements on the stack are strictly decreasing in value (and increasing in index)
# this enables an O(n) solution that beats 99.30% !
