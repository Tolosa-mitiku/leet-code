class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def helper(char, amount):
            z = (ord(char) - 97 + amount) % 26
            return chr(97 + z)
        count = 0
        ans = []
        for i in range(len(s)-1,-1,-1):
            count += shifts[i]
            ans.append(helper(s[i], count))
        ans.reverse()
        return "".join(ans)
            