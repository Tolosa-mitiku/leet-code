class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-(n//2), (n//2)+1)) if n % 2 == 1 else list(range(-1, -(n//2)-1,-1)) + list(range(1,(n//2)+1))