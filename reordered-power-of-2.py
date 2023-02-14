class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = list(str(n))
        ans = list(permutations(nums))
        for i in ans:
            if i[0] != "0" and bin(int("".join(i))).count("1") == 1:
                return True
        return False