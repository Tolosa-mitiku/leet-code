class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        for i in range(len(nums)-1,-1,-1):
            if not stack:
                stack.append(nums[i])
            else:
                while stack and stack[-1] > nums[i]:
                    for j in range(len(stack)):
                        if stack[j] > nums[i]:
                            temp = nums[i]
                            nums[i] = stack[j]
                            stack[j] = temp
                            break
                    for j in range(len(stack)):
                        nums[i+j+1] = stack[j]
                    return
                stack.append(nums[i])
        nums.reverse()