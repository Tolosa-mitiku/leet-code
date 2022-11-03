class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        
        ans = 0
        isodd = False
        for key in counter:
            temp = list(key)
            temp.reverse()
            temp = "".join(temp)
            if key == temp:
                if counter[temp] % 2 == 1:
                    ans += 2 * (counter[temp] - 1)
                    isodd = True
                else:
                    ans += 2 * (counter[temp])
            else:
                if temp in counter:
                    ans += 2 * min(counter[key], counter[temp])
        return ans + ( 2 * isodd)