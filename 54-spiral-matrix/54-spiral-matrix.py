class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        visited = set()
        x = 0
        y = 0
        dx, dy = 1, 0
        count = 0
        while count < len(matrix)*len(matrix[0]):
            ans.append(matrix[y][x])
            visited.add((y, x))
            if x + dx < 0 or x + dx >= len(matrix[0]) or y + dy < 0 or y + dy >= len(matrix) or (y+dy, x+dx) in visited:
                dx, dy = -1 * dy, dx
            x += dx
            y += dy
            count += 1
        return ans
            
            