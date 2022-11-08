class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in range(len(nums)):
            x ^= nums[i]
        differentiator = 0
        for i in range(33):
            if x & (1<<i) != 0:
                differentiator = i
                break
        ans1 = 0
        for i in range(len(nums)):
            if nums[i] & (1<<differentiator) != 0:
                ans1 ^= nums[i]
        return [ans1, x ^ ans1]
            