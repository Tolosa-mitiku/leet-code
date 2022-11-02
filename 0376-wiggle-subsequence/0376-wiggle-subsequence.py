class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        prev = "+"
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] < 0:
                prev = "+"
                break
            elif nums[i+1] - nums[i] > 0:
                prev = "-"
                break
        ans = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] < 0:
                curr = "-"
            elif nums[i+1] - nums[i] > 0:
                curr = "+"
            else:
                continue
                
            if curr != prev:
                ans += 1
            prev = curr
        return ans
                
                
                
            