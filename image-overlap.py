class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        first = []
        second = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    first.append((i,j))
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1:
                    second.append((i,j))
        ans = 0
        d = defaultdict(int)
        for a, b in first:
            for i, j in second:
                tr = (a-i, b-j)
                d[tr] += 1
                ans = max(ans, d[tr])
        return ans