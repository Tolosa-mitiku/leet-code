class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        secmatrix = [[False for i in range(len(mat[0])+1)] for j in range(len(mat)+1)]
        for i in range(len(mat)):
            prev = 0
            for j in range(len(mat[0])):
                prev += mat[i][j]
                secmatrix[i+1][j+1] = prev
                mat[i][j] = prev
        for i in range(len(mat[0])):
            prev = 0
            for j in range(len(mat)):
                prev += mat[j][i]
                secmatrix[j+1][i+1] = prev
        def helper(row1, col1):
            if row1 < 0:
                row = 0
            elif row1 >= len(mat):
                row = len(mat)
            else:
                row = row1
            if col1 < 0:
                col = 0
            elif col1 >= len(mat[0]):
                col = len(mat[0])
            else:
                col = col1
            return secmatrix[row][col]
        ans = [[False for i in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[i][j] = helper(i+k+1, j+k+1) + helper(i-k, j-k) - helper(i-k, j+k+1) - helper(i+k+1, j-k)
        return ans
                