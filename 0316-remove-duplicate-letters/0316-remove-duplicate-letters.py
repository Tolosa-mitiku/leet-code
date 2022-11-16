class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        lastind = defaultdict(int)
        
        for i in range(len(s)):
            lastind[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i]) and lastind[stack[-1]] > i:
                    visited.remove(stack.pop())
                visited.add(s[i])
                stack.append(s[i])
        return "".join(stack)