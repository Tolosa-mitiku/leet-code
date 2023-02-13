class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = 0
        y = 0
        for i in range(len(a)):
            if a[len(a)-1-i] == "1":
                x |= (1<<i)
        for i in range(len(b)):
            if b[len(b)-1-i] == "1":
                y |= (1<<i)  
        return bin(x+y)[2:]