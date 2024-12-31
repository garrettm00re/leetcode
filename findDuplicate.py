def findDuplicate(self, nums: List[int]) -> int:
    container = set()
    for n in nums:
        if n in container:
            return n
        container.add(n)
    return 'ERROR'
