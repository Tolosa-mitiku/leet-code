class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        ans = []
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans