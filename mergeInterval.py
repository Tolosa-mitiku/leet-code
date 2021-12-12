class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda arr: arr[0])
        count = 1
        while count < len(intervals):
            if intervals[count][0] <= intervals[count-1][1]:
                intervals[count-1][1] = max(intervals[count-1][1], intervals[count][1])
                intervals.pop(count)
            else:
                count += 1
        return intervals