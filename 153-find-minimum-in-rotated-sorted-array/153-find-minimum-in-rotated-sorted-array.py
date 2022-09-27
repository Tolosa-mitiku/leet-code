class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, best = 0, len(nums)-1, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                best = mid
                right = mid
            else:
                left = mid + 1
        return nums[left]