class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(i)
            else:
                if nums[i] < nums[stack[-1]]:
                    stack.append(i)
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack.pop())
        return ans