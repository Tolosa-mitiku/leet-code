class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[False for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(len(matrix)):
            prev = 0
            for j in range(len(matrix[0])):
                prev += matrix[i][j]
                self.matrix[i+1][j+1] = prev
                matrix[i][j] = prev
        for i in range(len(matrix[0])):
            prev = 0
            for j in range(len(matrix)):
                prev += matrix[j][i]
                self.matrix[j+1][i+1] = prev

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        return self.matrix[row2][col2] - self.matrix[row1][col2]- self.matrix[row2][col1] + self.matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)