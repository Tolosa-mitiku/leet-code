class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, prev = 0, 0, float("-inf")
        for right in range(len(nums)):
            if nums[right] != prev:
                nums[left] = nums[right]
                left += 1
            prev = nums[right]
        return left