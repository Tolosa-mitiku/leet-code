class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0]*num_people
        count = 1
        summ = 0
        ind = 0
        while count <= candies - summ:
            if ind < num_people:
                ans[ind] += count
                summ += count
                count += 1
                ind += 1
            else:
                ind = 0
        if ind < num_people:
            ans[ind] += (candies - summ)
        else:
            ans[0] += (candies - summ)
        return ans