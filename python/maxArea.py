#https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ptr1, ptr2 = 0, len(height) - 1
    area = 0
    while ptr1 < ptr2:
        h1, h2 = height[ptr1], height[ptr2]
        currArea = min(h1, h2) * (ptr2 - ptr1)
        area = max(area, currArea)
        if h1 == h2:
            ptr1 += 1
            ptr2 -= 1
        elif h1 > h2:
            ptr2 -= 1
        else:
            ptr1 += 1
    return area