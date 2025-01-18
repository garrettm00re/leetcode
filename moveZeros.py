# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    end = len(nums)
    while i < end:
        if nums[i] == 0:
            nums.append(0)
            nums.pop(i) # remove by index
            end -= 1
        else:
            i += 1
