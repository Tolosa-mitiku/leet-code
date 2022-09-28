class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = inf
        for i in range(len(timePoints)-1):        
            minn = timePoints[i].split(":")
            secminn = timePoints[i+1].split(":")
            diff = ((int(secminn[0]) - int(minn[0])+1) * 60) - int(minn[1]) - 60 + int(secminn[1])
            if diff < ans:
                ans = diff
        minn = timePoints[0].split(":")
        secminn = timePoints[-1].split(":")
        diff = ((24 - int(secminn[0]) + int(minn[0])+1) * 60) - int(secminn[1]) - 60 + int(minn[1])
        if diff < ans:
            ans = diff
        return ans
            