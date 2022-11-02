class Solution:
    def inbound(self, row, col, height, width):
        return 0 <= row < height and 0 <= col < width
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        adj = [[0,-1],[-1,0],[0,1],[1,0]]
        def backtrack(row, col, visited):
            nonlocal ans
            visited |= (1 << (len(grid) * col) + row)
            if grid[row][col] == 2:
                if visited == propervisited:
                    ans += 1
                return
            
            for dr, dc in adj:
                newrow = row + dr
                newcol = col + dc
                if self.inbound(newrow,newcol, len(grid), len(grid[0])) and grid[newrow][newcol] != -1 and (visited & (1 << (len(grid) * newcol) + newrow)) == 0:
                    backtrack(newrow, newcol, visited)
            
        startr, startc = 0, 0
        propervisited = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    continue    
                if grid[i][j] == 1:
                    startr, startc = i, j
                propervisited |= (1 << (len(grid) * j) + i)
        backtrack(startr, startc, 0)
        return ans