class Solution:
    def numberOfSteps(self, num: int) -> int:
        return num.bit_length() + bin(num).count("1") - 1 if num != 0 else 0