class NumArray:

    def __init__(self, nums: List[int]):
        prev = 0
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = prev
            prev += temp
        nums.append(prev)
        nums[0] = False
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)