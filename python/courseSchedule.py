# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for post, pre in prerequisites:
            prereqs[pre].append(post)

        def explore(node):
            callStack.add(node)
            remaining.discard(node)
            for child in prereqs[node]:
                if child in callStack:
                    return True
                if child in remaining and explore(child):
                    return True
            callStack.remove(node)
            return False

        remaining = set(prereqs.keys())
        while remaining:
            node = remaining.pop()
            callStack = set()
            if explore(node):
                return False
        return True
