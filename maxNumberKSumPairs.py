def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    counter = {}
    for num in nums:
        if not num in counter:
            counter[num] = 0
        counter[num] += 1
    
    sortKeys = sorted(counter.keys()) # counting sort is O(n), so this step is relatively inconsequential
    ptr = 0
    numPairs = 0
    while ptr < len(sortKeys) and sortKeys[ptr] < k:
        low = sortKeys[ptr]
        high = k - low
        if high in counter:
            if high != low:
                numPairs += min(counter[low], counter[high])
                del counter[low]
            else:
                numPairs += counter[high] // 2
            del counter[high]
        ptr += 1
    return numPairs