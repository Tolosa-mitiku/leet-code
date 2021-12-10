class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list1 = [0]*len(nums) 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[j] < nums[i]):
                    list1[i] += 1
        return list1