class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            for j in range(n):
                if (i == j) or (i + j == n-1):
                    ans += mat[i][j]
        return ans