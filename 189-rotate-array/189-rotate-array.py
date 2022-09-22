class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return 
        temp = list(nums)
        temp = temp * 2
        for i in range(len(nums)):
            nums[i] = temp[len(nums) + i - (k % len(nums))]