class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        
        charcounter = defaultdict(int)
        
        for i in s1:
            charcounter[i] += 1
        for j in s2:
            charcounter[j] += 1
            
        for char in charcounter:
            if charcounter[char] % 2 != 0:
                return -1
        
        count = defaultdict(int)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count[(s1[i], s2[i])] += 1
        
        ans = list(count.values())
        res = 0
        for i in range(len(ans)):
            res += ceil(ans[i] / 2)
        return res
        