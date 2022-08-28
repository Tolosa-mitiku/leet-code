class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)-1
        n = len(mat[0])-1
        j = 0
        for i in range(len(mat)+len(mat[0])-1):
            a = m
            b = j
            ans = []
            while a <= len(mat)-1 and b <= len(mat[0])-1:
                ans.append(mat[a][b])
                a+=1
                b+=1
            ans.sort()
            a = m
            b = j
            count = 0
            while a <= len(mat)-1 and b <= len(mat[0])-1:
                mat[a][b] = ans[count]
                count += 1
                a+=1
                b+=1
            if m > 0:
                m -= 1
            else:
                if j < n:
                    j += 1
        return mat