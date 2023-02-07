class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * i for i in nums]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -1 * heappop(nums)