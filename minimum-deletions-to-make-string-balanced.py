class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if len(stack)!=0 and stack[-1]=='b' and i != 'b':
                stack.pop()
                ans+=1
            else:
                stack.append(i)
        return ans