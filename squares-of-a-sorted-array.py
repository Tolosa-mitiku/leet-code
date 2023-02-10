class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            if nums[left] > nums[right]:
                ans.append(nums[left])
                left += 1
            else:
                ans.append(nums[right])
                right -= 1
        ans.reverse()
        return ans