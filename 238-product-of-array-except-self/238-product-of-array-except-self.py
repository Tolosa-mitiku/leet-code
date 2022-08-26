class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first = [1]
        second = [1]
        prefix = 1
        for i in nums:
            prefix *= i
            first.append(prefix)
        first.append(1)
        nums.reverse()
        prefix = 1
        for i in nums:
            prefix *= i
            second.append(prefix)
        second.append(1)
        second.reverse()
        ans = []
        for i in range(1, len(nums)+1):
            ans.append(first[i-1]*second[i+1])
        return ans
            
        