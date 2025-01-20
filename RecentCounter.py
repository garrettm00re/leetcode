# https://leetcode.com/problems/number-of-recent-calls/
# Fully optimized solution beats 75% of users with python3

class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.FRR = 0  # first request in range

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        beginning = t - 3000
        self.requests.append(t)
        while self.requests[self.FRR] < beginning:
            self.FRR += 1
        
        return len(self.requests) - self.FRR


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)