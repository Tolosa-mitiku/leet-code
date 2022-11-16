class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        for i in range(len(palindrome)):
            if palindrome[i] != "a" and not (len(palindrome) % 2 == 1 and i == len(palindrome) // 2):
                palindrome[i] = "a"
                return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)
            