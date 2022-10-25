class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def helper(ind,string):
            if ind >= len(s):
                ans.append(string)
                return
            if s[ind].isdigit():
                helper(ind + 1, string + s[ind])
            else:
                helper(ind + 1, string + s[ind].lower())
                helper(ind + 1, string + s[ind].upper())
        helper(0, "")
        return ans