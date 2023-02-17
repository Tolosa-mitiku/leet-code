class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n):
            if n == 1:
                return set(["()"])
            res = helper(n-1)
            ans = set()
            for parenthesis in res:
                for i in range(len(parenthesis)):
                    temp = list(parenthesis)
                    temp.insert(i, "()")
                    ans.add("".join(temp))
            return ans
        return helper(n)