def singleNumber(nums: list[int]) -> int:
    counter = {}
    for n in nums:
        if not n in counter:
            counter[n] = 0
        counter[n] += 1
        if counter[n] == 2:
            del counter[n]
    return next(iter(counter.keys()))