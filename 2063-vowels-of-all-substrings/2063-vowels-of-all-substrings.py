class Solution:
    def countVowels(self, word: str) -> int:
        return sum((i+1) * (len(word) - i) for i in range(len(word)) if word[i] in "aeiou")