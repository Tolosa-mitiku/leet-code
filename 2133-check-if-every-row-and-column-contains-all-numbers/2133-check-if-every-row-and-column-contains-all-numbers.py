class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        count = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] in count:
                    for k in count[matrix[i][j]]:
                        if k[0] == i or k[1] == j:
                            return False
                count[matrix[i][j]].append((i, j))
        return True