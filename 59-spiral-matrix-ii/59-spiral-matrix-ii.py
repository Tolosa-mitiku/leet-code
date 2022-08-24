class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[-1 for i in range(n)] for i in range(n)]
        x = 0
        y = 0
        dx, dy = 1, 0
        count = 0
        while count < n * n:
            ans[y][x] = count + 1
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n or ans[y + dy][x + dx] != -1:
                dx, dy = -1 * dy, dx
            x += dx
            y += dy
            count += 1
        return ans