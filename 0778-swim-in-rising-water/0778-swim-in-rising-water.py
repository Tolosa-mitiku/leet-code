class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        ans = 0
        adj = [[0,1],[1,0],[-1,0],[0,-1]]
        
        while heap:
            dist, i, j = heappop(heap)
            ans = max(ans, dist)
            if i == len(grid)-1 and j == len(grid)-1:
                return ans
            for dr, dc in adj:
                new_row = dr + i
                new_col = dc + j
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    heappush(heap, (grid[new_row][new_col], new_row, new_col))
                    
        return ans