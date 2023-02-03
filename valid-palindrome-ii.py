class Solution:
    def validPalindrome(self, s: str) -> bool:
        temp = list(s)
        poss_ans1 = []
        poss_ans2 = []
        l = 0
        r = len(s)-1
        while l <= r:
            if s[l] != s[r]:
                poss_ans1 = temp[:l] + temp[l+1:]
                poss_ans2 = temp[:r] + temp[r+1:]
                break
            l += 1
            r -= 1
        return poss_ans1 == poss_ans1[::-1] or poss_ans2 == poss_ans2[::-1]