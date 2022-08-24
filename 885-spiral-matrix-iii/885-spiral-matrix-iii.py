class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        x, y, dx, dy, count = cStart, rStart, 1, 0, 0
        seccount = 1

        while count < max(rows,cols) * max(rows,cols)*4:
            for i in range(2):
                for j in range(seccount):
                    if x >= 0 and x < cols and y >= 0 and y < rows:
                        ans.append([y, x])
                    count += 1
                    x+=dx
                    y+=dy
                dx, dy = -1*dy, dx
            seccount += 1
        return ans
            
        