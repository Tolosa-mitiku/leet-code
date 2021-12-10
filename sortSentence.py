class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        list1 = [""] * len(s)
        for i in s:
            list1[int(i[-1])-1] = i[:-1]
        return " ".join(list1)