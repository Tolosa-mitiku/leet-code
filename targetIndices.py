class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        list1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                list1.append(i)
        return list1
            