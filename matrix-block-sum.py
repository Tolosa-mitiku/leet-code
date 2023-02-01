class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        secmatrix = [[0 for i in range(len(mat[0])+1)] for j in range(len(mat)+1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                secmatrix[i+1][j+1] += mat[i][j] + secmatrix[i+1][j] + secmatrix[i][j+1] - secmatrix[i][j]
        def helper(row1, col1):
            if row1 < 0:
                row1 = 0
            elif row1 > len(mat):
                row1 = len(mat)
            if col1 < 0:
                col1 = 0
            elif col1 > len(mat[0]):
                col1 = len(mat[0])
            return secmatrix[row1][col1]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = helper(i+k+1, j+k+1) + helper(i-k, j-k) - helper(i-k, j+k+1) - helper(i+k+1, j-k)
        return mat