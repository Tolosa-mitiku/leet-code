class Solution:
    def __init__(self, w: List[int]):
        self.t = sum(w)
        self.probs = [w[0]/self.t]
        for i in w[1:]:
            self.probs.append(self.probs[-1] + (i / self.t))

    def pickIndex(self) -> int:
        rnd = random.random()
        idx = bisect.bisect(self.probs, rnd)
        return idx if idx != len(self.probs) else idx - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()