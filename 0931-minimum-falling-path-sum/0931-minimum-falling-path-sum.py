class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == len(matrix):
                return 0
            if j == -1 or j == len(matrix[0]):
                return float("inf")
            return matrix[i][j] + min(dp(i+1, j), dp(i+1, j-1), dp(i+1, j+1))
        return min(dp(0, i) for i in range(len(matrix[0])))
            
            