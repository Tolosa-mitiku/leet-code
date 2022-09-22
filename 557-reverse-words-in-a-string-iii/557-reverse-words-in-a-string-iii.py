class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            temp = list(s[i])
            temp.reverse()
            s[i] = "".join(temp)
        return " ".join(s)