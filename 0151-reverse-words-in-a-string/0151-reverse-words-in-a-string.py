class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        curr = []
        hasbeenadded = True
        for i in range(len(s)-1,-1,-1):
            if s[i] == " " and not hasbeenadded:
                curr.reverse()
                ans.append("".join(curr))
                curr = []
                hasbeenadded = True
            if s[i] != " ":
                curr.append(s[i])
                hasbeenadded = False
        if curr:
            curr.reverse()
            ans.append("".join(curr))
        return " ".join(ans)