class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right_sum = [0]
        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            left_sum.append(sum1)
            sum2 += nums[-1-i]
            right_sum.append(sum2)
        right_sum.reverse()
        for i in range(1,len(nums)+1):
            if left_sum[i-1] == right_sum[i]:
                return i -1
        return -1