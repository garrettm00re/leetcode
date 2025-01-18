#https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    start = 0
    end = k
    N = len(nums)
    subScore = mSub = sum(nums[:end]) 
    while end < N:
        subScore += nums[end] - nums[start]
        if subScore > mSub:
            mSub = subScore
        end += 1
        start += 1
    return float(mSub) / k