import random
class Solution:
    def __init__(self, nums: List[int]):
        self.number = nums
    def reset(self) -> List[int]:
        return self.number

    def shuffle(self) -> List[int]:
        ans = []
        sett = set(range(len(self.number)))
        g = randrange(0,len(self.number))
        while sett:
            while g not in sett:
                g = randrange(0,len(self.number))
            ans.append(self.number[g])
            sett.remove(g)
        return ans
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()