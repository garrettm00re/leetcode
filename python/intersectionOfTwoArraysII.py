# https://leetcode.com/problems/intersection-of-two-arrays-ii/

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    def makeCounter(nums):
        counter = {}
        for n in nums:
            if not n in counter:
                counter[n] = 0
            counter[n] += 1
        return counter

    c1, c2 = makeCounter(nums1), makeCounter(nums2)
    inBoth = set(c1.keys()) & set(c2.keys())
    ret = []
    for num in inBoth:
        ret.extend([num] * min(c1[num], c2[num]))
    return ret