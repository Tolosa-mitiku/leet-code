class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=3:
            return max(nums)
        def moneycalc(n):
            if n in dpdict:
                return dpdict[n]
            dpdict[n] = max(nums[n] + moneycalc(n+2), nums[n] + moneycalc(n+3))
            return dpdict[n]
        
        dpdict = {}
        dpdict[len(nums) -1] = nums[len(nums) -1]
        dpdict[len(nums) -2] = nums[len(nums) -2]
        dpdict[len(nums)] = 0
        ans1 = moneycalc(1)
        ans2 = moneycalc(2)
        dpdict = {}
        dpdict[len(nums) -3] = nums[len(nums) -3]
        dpdict[len(nums) -2] = nums[len(nums) -2]
        dpdict[len(nums)-1] = 0
        ans3 = moneycalc(0)
        return max(ans1, ans2, ans3)