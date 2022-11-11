class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, prev, isvisited = 0, float("-inf"), False
        for right in range(len(nums)):
            if nums[right] != prev:
                nums[left] = nums[right]
                left += 1
                isvisited = True
            elif nums[right] == prev and isvisited:
                nums[left] = nums[right]
                left += 1
                isvisited = False
            prev = nums[right]
        return left