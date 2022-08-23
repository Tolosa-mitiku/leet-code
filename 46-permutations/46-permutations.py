class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(n, arr):
            if n == len(nums)-1:
                for i in nums:
                    if i not in arr:
                        temp = arr.copy()
                        temp.append(i)
                ans.append(temp)
                return
            for i in nums:
                if i not in arr:
                    temp = arr.copy()
                    temp.append(i)
                    helper(n+1, temp)
        helper(0, [])
        return ans
                