class Solution:
    def countVowels(self, word: str) -> int:
        return sum((word[i] in "aeiou")*((i+1) * (len(word) - i)) for i in range(len(word)))