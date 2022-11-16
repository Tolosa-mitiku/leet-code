class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp = capacity
        ans = 0
        for i in range(len(plants)):
            temp -= plants[i]
            if temp >= 0:
                ans += 1
            else:
                temp = capacity - plants[i]
                ans += (2 *i)+ 1
        return ans