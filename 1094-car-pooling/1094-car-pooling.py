class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        A = []
        for i, j, k in trips:
            A.append([j , i])
            A.append([k , -1 * i])
        A.sort()
        curr = 0
        for i in A:
            curr += i[1]
            if curr > capacity:
                return False
        return True