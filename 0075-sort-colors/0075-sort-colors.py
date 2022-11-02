class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[right], nums[i] = nums[i], nums[right]
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1
            elif nums[i] == 1:
                nums[right], nums[i] = nums[i], nums[right]
                right += 1
        return nums