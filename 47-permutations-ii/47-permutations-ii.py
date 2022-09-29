class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def helper(arr):
            if len(arr) == len(nums):
                temp = []
                for i in arr:
                    temp.append(nums[i])
                ans.add(tuple(temp))
                return
            for i in range(len(nums)):
                if i not in arr:
                    temp = arr.copy()
                    temp.append(i)
                    helper(temp)
        helper([])
        return ans