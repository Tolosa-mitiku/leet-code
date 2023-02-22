class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        string = list(s)
        count = 0
        for i in range(len(s)):
            isOkay = True
            j = 0
            while j < len(s)-1:
                if string[j]=="0" and string[j+1]=="1":
                    string[j], string[j+1] = string[j+1], string[j]
                    isOkay = False
                    j+=1
                j+=1
            if isOkay:
                return count
            else:
                count += 1 
                    