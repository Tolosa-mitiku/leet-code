class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for i in ransomNote:
            if counter[i] > 0:
                counter[i] -= 1
            else:
                return False
        return True