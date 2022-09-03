class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = set()
        for i in range(k, 10):
            if i != 0:
                nums.add(i)
        for j in range(1, 9-k+1):
            nums.add(j)
        
            
        ans = []
        def helper(temp):
            if len(temp) == n:
                ans.append(int("".join(temp)))
                return
            if int(temp[-1]) + k <= 9 and k != 0:
                temp2 = temp.copy()
                temp2.append(str(int(temp[-1]) + k))
                helper(temp2)
            if 0 <= int(temp[-1]) - k or k == 0:
                temp3 = temp.copy()
                temp3.append(str(int(temp[-1]) - k))
                helper(temp3)
        for i in nums:
            helper([str(i)])       
        return ans
            