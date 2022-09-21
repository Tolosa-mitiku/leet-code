class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sett = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sett.add(i)
                count += nums[i]
        
        ans = []
        for query in queries:
            if abs(nums[query[1]] + query[0]) % 2 == 0:    
                if query[1] in sett:
                    count += query[0]
                    ans.append(count)
                else:
                    count += nums[query[1]] + query[0]
                    sett.add(query[1])
                    ans.append(count)
            else:
                if query[1] in sett:
                    count -= nums[query[1]]
                    sett.remove(query[1])
                    ans.append(count)
                else:
                    ans.append(count)
            nums[query[1]] += query[0]
        return ans