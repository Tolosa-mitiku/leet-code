class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans,surplus, start = 0, 0, 0
        for i in range(len(gas)):
            tank = gas[i] - cost[i]
            ans += tank
            surplus += tank
            if surplus < 0:
                start = i + 1
                surplus = 0
        return -1 if ans < 0 else start