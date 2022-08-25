class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = [0]*(len(s)+1)
        for i in shifts:
            if i[2]:
                ans[i[0]] += 1
                ans[i[1]+1] -= 1
            else:
                ans[i[0]] -= 1
                ans[i[1]+1] += 1
        res = []
        com_sum = 0
        for i in range(len(ans)-1):
            com_sum += ans[i]
            diff = ord(s[i]) - 97
            cur = (diff + com_sum) % 26
            res.append(chr(97 + cur))
        return "".join(res)
            