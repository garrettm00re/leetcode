class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sumToI(i):
            return  i * (i + 1) // 2 ## //2 ensures integer division which is critical for accuracy with large #s

        if n == 1:
            return maxSum
        if n == 2:
            return (maxSum + 1)//2

        jumpFxn = lambda jump: max(jump//2, 1)
        jump = maxSum//2
        total = 0
        curr = maxSum//2
        visited = set()
        bestVal = 1
        while True:
            if curr in visited:
                return bestVal
            visited.add(curr)

            ### CALCULATE TOTAL
            total = curr ** 2 #2 * sumToI(curr) - curr # just equals x^2
            lTail = index - curr + 1 # index of the leftmost one accounted for  by sumToI(curr)
            rTail = index + curr - 1 # ||
            if lTail > 0:
                total += lTail
            elif lTail < 0:
                total -= sumToI(abs(lTail))
            if rTail < n - 1:
                total += (n - 1 - rTail)
            elif rTail > n - 1:
                total -= sumToI(rTail - (n - 1))
            ### FINISH TOTAL CALCULATION
            
            if total == maxSum:
                return curr
            jump = jumpFxn(jump)
            if total < maxSum:
                if curr > bestVal:
                    bestVal = curr
                curr += jump
            elif total > maxSum:
                curr -= jump