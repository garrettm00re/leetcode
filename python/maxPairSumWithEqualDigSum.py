# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/

def maximumSum(nums: list[int]) -> int:
    def digitSum(num):
        ret = 0
        while num > 0:
            ret += num % 10
            num //= 10
        return ret

    sumdigitsIdx = {}
    mResult = -1
    for idx, n in enumerate(nums):
        nDigSum = digitSum(n)
        if not nDigSum in sumdigitsIdx:
            sumdigitsIdx[nDigSum] = []
        sumdigitsIdx[nDigSum].append(idx)
        if len(sumdigitsIdx[nDigSum]) > 2: # then its length is 3
            sumdigitsIdx[nDigSum].remove(min(sumdigitsIdx[nDigSum], key = lambda x : nums[x]))
        if len(sumdigitsIdx[nDigSum]) == 2:
            i1, i2 = sumdigitsIdx[nDigSum][0], sumdigitsIdx[nDigSum][1]
            pairSum = nums[i1] + nums[i2]
            if pairSum > mResult:
                mResult = pairSum

    return mResult
