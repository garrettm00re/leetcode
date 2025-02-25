import heapq
from typing import List


class Solution:
    # not my solution but I understand it. 
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i = 0
        j = len(costs) - 1
        pq1 = []
        pq2 = []

        ans = 0
        while k > 0:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1

            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')

            if t1 <= t2:
                ans += t1
                heapq.heappop(pq1)
            else:
                ans += t2
                heapq.heappop(pq2)

            k -= 1
        return ans
    
    import heapq

class Solution:
    # my solution, nominally slower but more intuitive. 
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = candidates, len(costs) - candidates - 1 # exclusive bounds
        totalCost = 0
        iterations = 0
        heap = [(costs[i], i) for i in range(len(costs)) if i < candidates or len(costs) - candidates <= i]
        heapq.heapify(heap)

        while left <= right and iterations < k: # (>= 2 * candidates) people left
            minEl, idx = heapq.heappop(heap)
            if idx < left:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            elif idx > right:
                heapq.heappush(heap, (costs[right], right))
                right -= 1
            totalCost += minEl
            iterations += 1

        while iterations < k:
            minEl, idx = heapq.heappop(heap)
            totalCost += minEl
            iterations += 1
        return totalCost