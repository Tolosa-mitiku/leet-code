class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for (x, y) in self.points:
            if abs(point[0] - x) != abs(point[1] - y) or point[0] == x or point[1] == y:
                continue
            if (x, point[1]) in self.points and (point[0], y) in self.points:
                ans += self.points[(point[0], y)] * self.points[(x, point[1])] * self.points[(x, y)]
        return ans
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)