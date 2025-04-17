#https://neetcode.io/problems/kth-largest-element-in-an-array

def findKthLargest(nums: list[int], k: int) -> int:
    import heapq
    N = len(nums)
    capacity = min(k, N - k + 1)
    minH = capacity == k
    heap = []
    for n in nums:
        el = n * (1 if minH else -1)
        heapq.heappush(heap, el)
        if len(heap) > capacity:
            m = heapq.heappop(heap)
    return (1 if minH else -1) * heapq.heappop(heap)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        k = int(sys.argv[-1])
        nums = [int(num) for num in sys.argv[1:-1]]
        assert isinstance(k, int)
        assert isinstance(nums, list)
        for n in nums:
            assert isinstance(n, int)
            
        print(findKthLargest(nums, k))

