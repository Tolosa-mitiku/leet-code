class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        ans = 0

        counter = defaultdict(int)

        for i in range(len(time)):
            counter[time[i] % 60] += 1

        for i in range(1, 30):
            if i in counter:
                ans += counter[i] * counter[60-i]
        
        ans += (counter[0] * (counter[0]-1)) // 2
        ans += (counter[30] * (counter[30]-1)) // 2

        return ans
