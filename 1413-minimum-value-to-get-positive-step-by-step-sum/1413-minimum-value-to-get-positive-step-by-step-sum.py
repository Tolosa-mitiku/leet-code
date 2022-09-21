class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = min(inf, nums[0])
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            ans = min(ans,nums[i])
        return 1 - ans if 1 - ans > 0 else 1