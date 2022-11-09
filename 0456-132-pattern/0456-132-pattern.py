class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        lastnum = float("-inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < lastnum:
                return True
            while stack and stack[-1] < nums[i]:
                lastnum = stack.pop()
            stack.append(nums[i])
        return False
        