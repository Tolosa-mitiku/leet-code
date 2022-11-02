class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(2 ** len(nums)):
            temp = []
            for j in range(len(nums)): 
                if i & (1<<j) != 0:
                    temp.append(nums[j])
            temp.sort()
            ans.add(tuple(temp))
        return ans