# elegant solution -- > O(N) runtime, O(1) space and very easy to understand
def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

# clunky but functional. O(N) runtime, O(1) space
def increasingTriplet(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    n = len(nums)
    i, j = 0, 1
    while j < n:
        if nums[j] > nums[i]:
            break
        j, i = j + 1, i + 1

    k = j + 1
    mindex = i

    while n > k:
        if nums[i] < nums[j] < nums[k]:
            return True
        else:
            if nums[k] < nums[mindex]:
                mindex = k
            if nums[j] > nums[k] and nums[mindex] < nums[k]: # nums k is less than nums j, and constraints are satisfied
                j = k
                i = mindex
            k += 1
    return False
###  doesn't work --> captures initial idea perfectly
# mistake: I oversimplified the problem (and didn't check my logic before submitting)

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i, j = 0, 1
        mindex = 1
        n = len(nums)
        while n > j and nums[i] >= nums[j]:
            if nums[mindex] < nums[j]:
                i = mindex
                break
            else:
                mindex = min([mindex, j], key = lambda x : nums[x])
                j += 1
        k = j + 1
        while k < n:
            if nums[k] > nums[j]:
                return True # i , j, k
            k += 1
        return False