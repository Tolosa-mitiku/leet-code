class Solution:
    def removeOccurrences(self, word: str, substring: str) -> str:
        while substring in word:
            for i in range(len(word)-len(substring)+1):
                found = False
                for letter in range(len(substring)):
                    if word[i+letter] != substring[letter]:
                        break
                    if letter == len(substring)-1:
                        found = True
                        word = word[0:i] + word[letter+i+1:]
                if found:
                    break
        return word