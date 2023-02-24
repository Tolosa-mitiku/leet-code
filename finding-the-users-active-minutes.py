class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)

        for id, time in logs:
            UAM[id].add(time)
        
        counter = {}

        for id in UAM:
            counter[id] = len(UAM[id])

        
        count = Counter(counter.values())

        ans = [0] * k

        for i in count:
            ans[i-1] = count[i]

        return ans
        