class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = defaultdict(int)
        for i in arr:
            count[i] += 1
        reps = []
        for i in count:
            reps.append(count[i])
        reps.sort(reverse=True)
        count2 = 0
        count3 = 0
        while count2 < len(arr) //2:
            count2 += reps[count3]
            count3 +=1
        return count3
            
            