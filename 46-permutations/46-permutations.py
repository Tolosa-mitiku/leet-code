class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(arr):
            if len(arr) == len(nums):
                ans.append(arr)
                return
            for i in nums:
                if i not in arr:
                    temp = arr.copy()
                    temp.append(i)
                    helper(temp)
        helper([])
        return ans    
                