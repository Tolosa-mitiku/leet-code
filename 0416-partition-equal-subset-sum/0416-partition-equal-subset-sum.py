class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target /= 2
        
        @cache
        def dp(ind, summ):
            if summ == target:
                return True
            if summ > target or ind == len(nums):
                return False

            return (dp(ind+1, summ + nums[ind]) or dp(ind+1, summ))
        return dp(0, 0)