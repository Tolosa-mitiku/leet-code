class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return [dup, i+1]
            