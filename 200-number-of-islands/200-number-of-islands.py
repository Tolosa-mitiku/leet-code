class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        bound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        Adj = [[0,1], [1,0],[-1, 0],[0,-1]]
        
        def helper(x, y):
            queue = deque([(x, y)])
            while queue:
                row, col = queue.popleft()
                for nrow, ncol in Adj:
                    if bound(nrow+row, ncol+col) and grid[nrow+row][ncol+col] == "1":
                        grid[nrow+row][ncol+col] = "#"
                        queue.append((nrow+row, ncol+col))
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    helper(i, j)
                    ans += 1
        return ans