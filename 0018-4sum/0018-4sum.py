class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                second_target = target - nums[i] - nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == second_target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                    elif nums[left] + nums[right] < second_target:
                        left += 1
                    else:
                        right -= 1
        return ans