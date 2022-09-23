class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        ans = []
        def helper(string, ind):
            if ind == len(digits):
                if string:
                    ans.append("".join(string))
                return
            for i in digitToChar[digits[ind]]:
                string.append(i)
                helper(string, ind+1)
                string.pop()
                
        helper([], 0)
        return ans