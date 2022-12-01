class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1 and obstacleGrid[i][j] != 1:
                return 1
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            return dp(i+1, j) + dp(i, j+1)
        
        return dp(0, 0)