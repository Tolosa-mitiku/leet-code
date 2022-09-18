class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        adj = [[1,0], [1,1], [1, -1]]
        bound = lambda row, col: 0 <= row < len(matrix) and 0 <= col < len(matrix)
        
        def helper(row, col):
            if (row, col) in mydict:
                return mydict[(row, col)]
            val = float("inf")
            for i in adj:
                new_row = row + i[0]
                new_col = col + i[1]
                if bound(new_row, new_col):
                    val = min(val, matrix[row][col] + helper(new_row, new_col))
            mydict[(row, col)] = val
            return mydict[(row, col)]
        mydict = {}
        for i in range(len(matrix[0])):
            mydict[(len(matrix)-1, i)] = matrix[len(matrix)-1][i]
        ans = float("inf")
        for i in range(len(matrix[0])):
            ans = min(ans, helper(0,i))
        return ans