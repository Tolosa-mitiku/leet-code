class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i] = [points[i][0], points[i][1], (points[i][0] ** 2) + (points[i][1] ** 2)]
        points.sort(key=lambda arr: arr[2])
        for i in range(len(points)):
            points[i].pop()
        return points[:k]