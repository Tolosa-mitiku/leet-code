class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            hourcount = bin(i).count("1")
            for j in range(60):
                minutecount = bin(j).count("1")
                if hourcount + minutecount == turnedOn:
                    hour = str(i) 
                    minute = str(j) if j >= 10 else "0" + str(j)
                    time = hour + ":" + minute
                    ans.append(time)
        return ans