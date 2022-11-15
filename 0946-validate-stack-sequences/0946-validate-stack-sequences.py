class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        curr = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[curr]:
                stack.pop()
                curr += 1
        return len(stack) == 0