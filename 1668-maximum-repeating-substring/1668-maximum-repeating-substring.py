class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        def checker(i, j):
            count = 0
            for k in range(i, j):
                if j > len(sequence) or sequence[k] != word[count]:
                    return False
                count += 1
            return True
        
        ans = 0
        count = 0
        for i in range(len(word)):
            count = 0
            for j in range(i,len(sequence), len(word)):
                if checker(j, j + len(word)):
                    count += 1
                else:
                    ans = max(ans, count)
                    count = 0
            ans = max(ans, count)
        return ans
                    