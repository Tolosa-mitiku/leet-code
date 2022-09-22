class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        for i in range(0, len(s), k):
            temp = i + k if i + k < len(s) else len(s)
            if (i / k) % 2 == 1:
                temp2 = []
                for j in range(i, temp):
                    ans.append(s[j])
                    temp2.append(s[j])
            else:
                temp2 = []
                for j in range(temp-1, i-1,-1):
                    ans.append(s[j])
                    temp2.append(s[j])
        return "".join(ans)
            